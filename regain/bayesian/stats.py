"""Statistical functions."""
import numpy as np
from sklearn.utils.extmath import squared_norm


def lognormal_pdf(x, mu, sigma):
    """Lognormal pdf.

    Equivalent to
    stats.lognorm.pdf(x, loc=0, s=sigma, scale=np.exp(mu))

    Reference
    ---------
    https://stackoverflow.com/questions/8870982/how-do-i-get-a-lognormal-distribution-in-python-with-mu-and-sigma
    """
    return np.exp(-0.5 * ((np.log(x) - mu) / sigma) ** 2) \
        / (x * sigma * np.sqrt(2 * np.pi))


def lognormal_logpdf(x, mu, sigma):
    """Lognormal log pdf.

    Equivalent to
    stats.lognorm.logpdf(x, loc=0, s=sigma, scale=np.exp(mu))
    """
    return np.log(lognormal_pdf(x, mu, sigma))


def lognstat(mean, variance):
    """A lognormal distribution with mean m and variance v has mu sigma as."""
    m2 = mean * mean
    mu = np.log(m2 / np.sqrt(variance + m2))
    sigma = np.sqrt(np.log(variance / m2 + 1))
    return mu, sigma


def log_lik_frob(S, D, variance):
    """Frobenius norm log likelihood."""
    logl = -0.5 * (S.size * np.log(2. * np.pi * variance)
                   + squared_norm(S - D) / variance)
    return logl


def log_likelihood_normal(x, mean, var):
    """Normal log likelihood."""
    logl = -0.5 * (np.log(2 * np.pi * var) + (x - mean) ** 2 / var)
    # logl2 = stats.norm.logpdf(x, loc=mean, scale=np.sqrt(var))
    # assert logl == logl2, (logl, logl2)
    return logl
