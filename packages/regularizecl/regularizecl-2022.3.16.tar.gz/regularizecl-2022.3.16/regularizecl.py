# author: Nicolas Tessore <n.tessore@ucl.ac.uk>
# license: MIT
r'''

Regularize angular power spectra (:mod:`regularizecl`)
======================================================

This is a minimal Python package for regularising the angular power spectra of
multiple correlated spherical random fields.

The package can be installed using pip::

    pip install regularizecl

Then import the :func:`~regularizecl.regularize_cls` function from the package::

    from regularizecl import regularize_cls

Current functionality covers the absolutely minimal use case.  Please open an
issue on GitHub if you would like to see anything added.


Reference/API
-------------

.. autosummary::
   :toctree: api
   :nosignatures:

   regularize_cls

'''

__version__ = '2022.3.16'

__all__ = [
    'regularize_cls',
]

import numpy as np
from sortcl import enumerate_cls, cl_indices


def cov_clip(cov):
    '''covariance matrix from clipped negative eigenvalues'''

    # set negative eigenvalues to zero
    w, v = np.linalg.eigh(cov)
    w[w < 0] = 0

    # put matrix back together
    cov = np.einsum('...ij,...j,...kj->...ik', v, w, v)

    # fix the upper triangular part of the matrix to zero
    cov[(...,) + np.triu_indices(w.shape[-1], 1)] = 0

    # return the regularised covariance matrix
    return cov


def cov_nearest(cov, niter=20):
    '''covariance matrix from nearest correlation matrix

    Uses the algorithm of Higham (2000).

    '''

    # size of the covariance matrix
    s = np.shape(cov)
    n = s[-1]

    # make a copy to work on
    corr = np.copy(cov)

    # view onto the diagonal of the correlation matrix
    diag = corr.reshape(s[:-2] + (-1,))[..., ::n+1]

    # set correlations with nonpositive diagonal to zero
    good = (diag > 0)
    corr *= good[..., np.newaxis, :]
    corr *= good[..., :, np.newaxis]

    # get sqrt of the diagonal for normalization
    norm = np.sqrt(diag)

    # compute the correlation matrix
    np.divide(corr, norm[..., np.newaxis, :], where=good[..., np.newaxis, :], out=corr)
    np.divide(corr, norm[..., :, np.newaxis], where=good[..., :, np.newaxis], out=corr)

    # indices of the upper triangular part of the matrix
    triu = (...,) + np.triu_indices(n, 1)

    # always keep upper triangular part of matrix fixed to zero
    # otherwise, Dykstra's correction points in the wrong direction
    corr[triu] = 0

    # find the nearest covariance matrix with given diagonal
    dyks = np.zeros_like(corr)
    proj = np.empty_like(corr)
    for k in range(niter):
        # apply Dykstra's correction to current result
        np.subtract(corr, dyks, out=proj)

        # project onto positive semi-definite matrices
        w, v = np.linalg.eigh(proj)
        w[w < 0] = 0
        np.einsum('...ij,...j,...kj->...ik', v, w, v, out=corr)

        # keep upper triangular part fixed to zero
        corr[triu] = 0

        # compute Dykstra's correction
        np.subtract(corr, proj, out=dyks)

        # project onto matrices with unit diagonal
        diag[good] = 1

    # put the normalisation back to convert correlations to covariance
    np.multiply(corr, norm[..., np.newaxis, :], out=corr)
    np.multiply(corr, norm[..., :, np.newaxis], out=corr)

    # return the regularised covariance matrix
    return corr


def regularize_cls(cls, method='nearest'):
    '''regularize angular power spectra

    Regularises a complete set of angular power spectra such that at every
    angular mode number :math:`l`, the matrix :math:`C_l^{ij}` is a valid
    positive semi-definite covariance matrix.

    Parameters
    ----------
    cls : (N,) list of array_like
        List of angular power spectra in HEALPix order (see :mod:`sortcl`).
        Missing entries can be set to ``None``.
    method : str, optional
        Regularisation method to apply.  Valid methods are:

        * ``'nearest'`` (default)
        * ``'clip'``

        For details, see notes below.

    Returns
    -------
    reg : (N,) list of array_like
        List of regularised angular power spectra.

    Notes
    -----
    This function constructs and regularises the stack of covariance matrices
    :math:`C_l^{ij}` with :math:`l` the leading axis.  The implemented methods
    for regularisation are as follows.

    ``nearest``
        Divide the rows and columns of the given matrix by the square root of
        its diagonal, then find the nearest correlation matrix to the result
        using the algorithm of Higham [1]_.  This keeps the diagonals (i.e. the
        auto-angular power spectra) fixed, but requires all of them to be
        nonnegative.
    ``clip``
        Compute the eigendecomposition of the given matrix and set all negative
        eigenvalues to zero.

    References
    ----------
    .. [1] N. J. Higham, Computing the Nearest Correlation Matrix – A Problem
           from Finance, IMA J. Numer. Anal. 22, 329–343, 2002

    '''

    # number of fields
    n = int((2*len(cls))**0.5)
    if len(cls) != n*(n+1)//2:
        raise TypeError(f'number of cls is not a triangle number: {len(cls)}')

    # maximum length in input cls
    k = max(len(cl) for cl in cls if cl is not None)

    # this is the covariance matrix of cls
    # the leading dimension is k, then it is a n x n covariance matrix
    # missing entries are zero, which is the default value
    cov = np.zeros((k, n, n))

    # fill the matrix up by going through the cls in order
    # if the cls list is ragged, some entries at high l may remain zero
    # only fill the lower triangular part, everything is symmetric
    for i, j, cl in enumerate_cls(cls):
        if cl is not None:
            cov[:len(cl), j, i] = cl

    # use cholesky() as a fast way to check for positive semi-definite
    # if it fails, the matrix of cls needs regularisation
    # otherwise, the matrix is pos. def. and the cls are good
    try:
        np.linalg.cholesky(cov + np.finfo(0.).tiny)
    except np.linalg.LinAlgError:
        pass
    else:
        return cls

    # regularise the cov matrix using the chosen method
    if method == 'clip':
        cov = cov_clip(cov)
    elif method == 'nearest':
        cov = cov_nearest(cov)
    else:
        raise ValueError(f'unknown method "{method}"')

    # gather regularised cls from array
    # convert matrix slices to contiguous arrays for type safety
    cls = []
    for i, j in zip(*cl_indices(n)):
        cls.append(np.ascontiguousarray(cov[:, j, i]))

    # return the regularised cls
    return cls
