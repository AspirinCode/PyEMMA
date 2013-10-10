################################################################################
# Assessment tools
################################################################################
from scipy.sparse import issparse
from scipy.sparse.sputils import isdense

import dense.assessment
import dense.decomposition

import sparse.assessment
import sparse.decomposition

import numpy as np


_type_not_supported = \
    TypeError("given matrix is not a numpy.ndarray or a scipy.sparse matrix.")

def is_transition_matrix(T, tol=1e-15):
    """
    True if T is a transition matrix
    
    Parameters
    ----------
    T : numpy.ndarray, shape(d, d) or scipy.sparse matrix
        Matrix to check
    tol : float
        tolerance to check with
    
    Returns
    -------
    Truth value: bool
        True, if T is positive and normed
        False, otherwise
    
    """
    if issparse(T):
        return sparse.assessment.is_transition_matrix(T, tol)
    elif isdense(T):
        return dense.assessment.is_stochastic_matrix(T, tol)
    else:
        raise TypeError("T is not a numpy.ndarray or a scipy.sparse matrix.")
      

def is_rate_matrix(K, tol=1e-15):
    r"""True if K is a rate matrix
    """
    if issparse(K):
        return sparse.assessment.is_rate_matrix(K, tol)
    elif isdense(K):
        return dense.assessment.is_rate_matrix(K, tol)
    else:
        raise _type_not_supported


# TODO: Implement in Python directly
def is_ergodic(T, tol=1e-15):
    r"""True if T is connected (irreducible) and aperiodic
    """

# TODO: martin: Implement in Python directly
def is_reversible(T, mu=None, tol=1e-15):
    r"""True if T is a transition matrix
        mu : tests with respect to this stationary distribution
    """
    
    
################################################################################
# Eigenvalues and eigenvectors
################################################################################

# DONE: ben: Implement in Python directly
def mu(T):
    r"""Compute stationary distribution of stochastic matrix T. 
      
    The stationary distribution is the left eigenvector corresponding to the 
    non-degenerate eigenvalue :math: `\lambda=1`.

    Input
    -----
    T : numpy array, shape(d,d) or scipy.sparse matrix
        Transition matrix (stochastic matrix).

    Returns
    -------
    mu : numpy array, shape(d,)      
        Vector of stationary probabilities.

    """
    if issparse(T):
        return sparse.decomposition.mu(T)
    elif isdense(T):
        return dense.decomposition.mu(T)
    else: 
        raise _type_not_supported


# TODO: Implement in Python directly
def mu_sensitivity(T):
    r"""compute the sensitivity matrix of the stationary distribution of T"""

# DONE: ben: Implement in Python directly
def statdist(T):
    r"""Compute stationary distribution of stochastic matrix T. 
      
    The stationary distribution is the left eigenvector corresponding to the 
    non-degenerate eigenvalue :math: `\lambda=1`.

    Input
    -----
    T : numpy array, shape(d,d) or scipy.sparse matrix
        Transition matrix (stochastic matrix).

    Returns
    -------
    mu : numpy array, shape(d,)      
        Vector of stationary probabilities.

    """
    statdist=mu(T)
    return statdist


# TODO: Implement in Python directly
def statdist_sensitivity(T):
    r"""compute the sensitivity matrix of the stationary distribution of T
    """    
# TODO: Martin move implementation to dense.decomposition create implementation in sparse.decomposition
def eigenvalues(T, k=None):
    r"""computes the eigenvalues

        T : transition matrix
        k : int (optional) or tuple of ints
            Compute the first k eigenvalues of T.
    """
    if issparse(T):
        return sparse.decomposition.eigenvalues(T, k)
    elif isdense(T):
        return dense.decomposition.eigenvalues(T, k)
    else:
        raise _type_not_supported


# TODO: Implement in Python directly
def eigenvalues_sensitivity(T, k=None):
    r"""computes the sensitivity of the specified eigenvalue

        k : int (optional)
            Compute the sensitivity of the first k eigenvalues of T.
    """

# TODO: ben: Implement in Python directly
def timescales(T, tau=1, k=None):
    r"""Compute implied time scales of given transition matrix

        T: transition matrix
        tau: lag time
        k : int (optional)
            Compute the first k implied time scales of T.
    """

# DONE: ben: Implement in Python directly
def eigenvectors(T, k=None, right=True):
    r"""Compute eigenvectors of given transition matrix.

    Eigenvectors are computed using the scipy interface 
    to the corresponding LAPACK/ARPACK routines.    

    Input
    -----
    T : numpy.ndarray, shape(d,d) or scipy.sparse matrix
        Transition matrix (stochastic matrix).
    k : int (optional) or array-like 
        For integer k compute the first k eigenvalues of T
        else return those eigenvector sepcified by integer indices in k.

    Returns
    -------
    eigvec : numpy.ndarray, shape=(d, n)
        The eigenvectors of T ordered with decreasing absolute value of
        the corresponding eigenvalue. If k is None then n=d, if k is
        int then n=k otherwise n is the length of the given indices array.

    """
    if issparse(T):
        return sparse.decomposition.eigenvectors(T, k=k, right=right)
    elif isdense(T):
        return dense.decomposition.eigenvectors(T, k=k, right=right)
    else: 
        raise _type_not_supported
    

# TODO: Implement in Python directly
def eigenvectors_sensitivity(T, k=None, right=True):
    r"""Compute eigenvector snesitivity of T

    k : int (optional)
        Compute eigenvectors to 
    right : bool
        If True compute right eigenvectors, otherwise compute left eigenvectors.
    """

# TODO: ben: Implement in Python directly
def rdl_decomposition(T, k=None, norm='standard'):
    r"""Compute the decomposition into left and right eigenvectors.
    
    Parameters
    ----------
    T : ndarray or sparse matrix
        Transition matrix    
    k : int (optional)
        Number of eigenvector/eigenvalue pairs
    norm: {'standard', 'reversible'}
        standard: (L'R) = Id, L[:,0] is a probability distribution,
            the stationary distribution mu of T. Right eigenvectors
            R have a 2-norm of 1.
        reversible: R and L are related via L=L[:,0]*R.
                         
    Returns
    -------
    w : (M,) ndarray
        The eigenvalues, each repeated according to its multiplicity
    L : (M, M) ndarray
        The normalized (with respect to R) left eigenvectors, such that the 
        column L[:,i] is the left eigenvector corresponding to the eigenvalue
        w[i], dot(L[:,i], T)=w[i]*L[:,i]
    R : (M, M) ndarray
        The normalized ("unit length") right eigenvectors, such that the 
        column R[:,i] is the right eigenvector corresponding to the eigenvalue 
        w[i], dot(T,R[:,i])=w[i]*R[:,i]
      
    """
    if issparse(T):
        return sparse.decomposition.rdl_decomposition(T, k=k, norm=norm)
    elif isdense(T):
        return dense.decomposition.rdl_decomposition(T, k=k, norm=norm)
    else: 
        raise _type_not_supported
    
# TODO: Implement in Python directly
def mfpt(T, i):
    r"""Computes vector of mean first passage times for given target state.

    Parameters
    ----------
    P : ndarray, shape=(n,n) 
        Transition matrix.
    i : Integer
        Target state for mfpt calculation.

    Returns
    -------
    x : ndarray, shape=(n,)
        Vector of mean first passage times.

   """

# TODO: Implement in Python directly
def mfpt_sensitivity(T, i):
    r"""Compute sensitivity of mfpt
    """


################################################################################
# Expectations
################################################################################

# TODO: martin: Implement in Python directly
def expectation(T, a):
    r"""computes the expectation value of a
    
    Parameters
    ----------
        T : matrix
        a : scalar
        
        
    Returns
    -------
        expectation value of a
    """
    
    # check a is contained in T
    
    # calculate E[a]
    

# TODO: Implement in Python directly
def expectation_sensitivity(T, a):    
    r"""computes the sensitivity of the expectation value of a
    """

# TODO: ben: Implement in Python directly
def expected_counts(p0, T, N):
   r"""Compute expected transition counts for Markov chain with n steps. 

   Expected counts are computed according to ..math::
   
                                \sum_{k=0}^n-1 diag(p^{T} T^{k})*T  n \geq 1
   E[C^{(n)}(x_0,\dotsc,x_n)]=   
                                0                                  n=0

   Parameters
   ----------
   p0 : numpy array, shape=(n,)
      Starting (probability) vector of the chain, numpy.sum(p)=1.0.
   T : numpy array, shape=(n,n)
      Transition matrix for the chain. T\geq 0, numpy.sum(T,axis=1)=(1,...,1)
   N : int
      Number of steps for chain.

   Returns
   --------
   EC : numpy array, shape=(n,n)
       Expected value for transition counts after a propagation of n steps. 

   """

# TODO: ben: Implement in Python directly
def expected_counts_stationary(P, N, mu=None):
    """
   Expected transition counts for Markov chain in equilibrium. 

   Since mu is stationary for T we have 

      E(C^{(n)})(x_0,dotsc,x_{n-1})=n diag(mu)*T.

   Parameters
   -----------
   P : numpy array, shape=(n,n)
      Transition matrix for the chain. T\geq 0, numpy.sum(T,axis=1)=(1,...,1)
   n : int
      Number of steps for chain.
   mu : numpy array, shape=(n,)
      Stationary probability vector of the chain, numpy.sum(p)=1.0. 
      If mu is not specified it will be computed via diagonalization of T.  

   Returns:
   --------
   EC : numpy array, shape=(n,n)
       Expected value for transition counts after a propagation of n steps. 

   """

################################################################################
# Fingerprints
################################################################################

# TODO: martin: Implement in Python directly
def autocorrelation(P, obs):
    """Compute dynamical fingerprint crosscorrelation.

    The dynamical fingerprint autocorrelation is the timescale
    amplitude spectrum of the autocorrelation of the given observables 
    under the action of the dynamics P

    Parameters
    ----------
    P : ndarray, shape=(n, n) or scipy.sparse matrix
       Transition matrix
    obs : ndarray, shape=(n,)
        Vector representing observable on discrete states

    Returns
    -------

    """

# TODO: Implement in Python directly
def crosscorrelation(P, obs1, obs2):
    """Compute dynamical fingerprint crosscorrelation.

    The dynamical fingerprint crosscorrelation is the timescale
    amplitude spectrum of the crosscorrelation of the given observables 
    under the action of the dynamics P

    Parameters
    ----------
    P : ndarray, shape=(n, n) or scipy.sparse matrix
       Transition matrix
    obs1 : ndarray, shape=(n,)
        Vector representing observable on discrete states
    obs2 : ndarray, shape=(n,)
        Vector representing observable on discrete states

    Returns
    -------

    """

# TODO: Implement in Python directly
def perturbation(P, obs, p0):
    """

    Parameters
    ----------
    P : ndarray, shape=(n, n) or scipy.sparse matrix
       Transition matrix
    obs : ndarray, shape=(n,)
        Vector representing observable on discrete states
    p0 : ndarray, shape=(n,)
        Vector of initial probabilities.

    Returns :
    ---------
    
    """

################################################################################
# PCCA
################################################################################

# TODO: Implement in Python directly
def pcca(T, n):
    """
        returns a PCCA object
        T: transition matrix
        n: number of metastable processes
    """


################################################################################
# Transition path theory
################################################################################

# TODO: Implement in Python directly
def committor(P, A, B, forward=True):
    """Compute the committor between sets of microstates.

    Parameters
    ----------
    P : ndarray, shape=(n, n) or scipy.sparse matrix
        Transition matrix
    A : array_like
        List of integer state labels for set A
    B : array_like
        List of integer state labels for set B
    forward : bool
        If True compute the forward committor, else
        compute the backward committor.

    Returns
    -------
    x : ndarray, shape=(n, )
        Commitor vector.

    """

# TODO: Implement in Python directly
def committor_sensitivity(P, A, B, forward=True):
    """Compute the committor between sets of microstates.

    Parameters
    ----------
    P : ndarray, shape=(n, n) or scipy.sparse matrix
        Transition matrix
    A : array_like
        List of integer state labels for set A
    B : array_like
        List of integer state labels for set B
    forward : bool
        If True compute the forward committor, else
        compute the backward committor.

    Returns
    -------
    x : ndarray, shape=(n, )
        Commitor vector.

    """

# TODO: Translate from stallone
def tpt(T, A, B):
    """
        returns a TPT object
    """