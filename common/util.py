import math

import numpy as np
import scipy.stats
import scipy.special

from common.Pmf import Pmf


ROOT2 = math.sqrt(2)


def make_mixture(meta_pmf, name='mix'):
    mix = Pmf(name=name)
    for pmf, p1 in meta_pmf.iter_items():
        for x, p2 in pmf.iter_items():
            mix.incr(x, p1 * p2)
    mix.normalize()
    return mix


def make_cdf_from_list(values, name=''):
    pmf = Pmf()
    for value in values:
        pmf.incr(value)
    pmf.normalize()
    return pmf.make_cdf(name=name)


def make_pmf_from_list(values, name=''):
    pmf = Pmf(name=name)
    for value in values:
        pmf.incr(value)
    pmf.normalize()
    return pmf


def make_gaussian_pmf(mu, sigma, num_sigmas, n=101):
    pmf = Pmf()
    low = mu - num_sigmas * sigma
    high = mu + num_sigmas * sigma
    for x in np.linspace(low, high, n):
        p = scipy.stats.norm.pdf(x, mu, sigma)
        pmf.set(x, p)
    pmf.normalize()
    return pmf


def eval_poisson_pmf(lam, k):
    # return lam ** k * math.exp(-lam) / math.factorial(k)
    return scipy.stats.poisson.pmf(k, lam)


def eval_exponential_pdf(lam, x):
    return lam * math.exp(-lam * x)


def eval_gaussian_pdf(x, mu, sigma):
    return scipy.stats.norm.pdf(x, mu, sigma)


def eval_gaussian_log_pdf(x, mu, sigma):
    return scipy.stats.norm.logpdf(x, mu, sigma)


def gaussian_cdf(x, mu=0, sigma=1):
    return standard_gaussian_cdf(float(x - mu) / sigma)


def eval_binomial_pmf(k, n, p):
    return scipy.stats.binom.pmf(k, n, p)


def make_poisson_pmf(lam, high, step=1):
    pmf = Pmf()
    for k in range(0, high + 1, step):
        p = eval_poisson_pmf(lam, k)
        pmf.set(k, p)
    pmf.normalize()
    return pmf


def make_exponential_pmf(lam, high, n=200):
    xs = np.linspace(0, high, n)
    probs = [eval_exponential_pdf(lam, x) for x in xs]
    pmf = Pmf(values=xs, probs=probs)
    return pmf


def standard_gaussian_cdf(x):
    return (scipy.special.erf(x / ROOT2) + 1) / 2


def pmf_prob_less(pmf_1, pmf_2):
    total = 0.0
    for v1, p1 in pmf_1.iter_items():
        for v2, p2 in pmf_2.iter_items():
            if v1 < v2:
                total += p1 * p2
    return total


def median_ipr(xs, p):
    cdf = make_cdf_from_list(xs)
    median = cdf.percentile(50)
    alpha = (1 - p) / 2.0
    ipr = cdf.value(1 - alpha) - cdf.value(alpha)
    return median, ipr


def median_s(xs, num_sigmas):
    half_p = standard_gaussian_cdf(num_sigmas) - 0.5
    median, ipr = median_ipr(xs, half_p * 2)
    s = ipr / 2.0 / num_sigmas
    return median, s


def mean(t):
    return float(sum(t)) / len(t)


def var(t, mu=None):
    mu = mu if mu else mean(t)
    dev2 = [(x - mu)**2 for x in t]
    v = mean(dev2)
    return v


def mean_var(t):
    mu = mean(t)
    v = var(t, mu)
    return mu, v
