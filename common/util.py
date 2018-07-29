import numpy as np
import pandas as pd
import scipy.stats
import math

from common.Pmf import Pmf


def make_mixture(meta_pmf, name='mix'):
    mix = Pmf(name=name)
    for pmf, p1 in meta_pmf.iter_items():
        for x, p2 in pmf.iter_items():
            mix.incr(x, p1 * p2)
    mix.normalize()
    return mix


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
    return lam ** k * math.exp(-lam) / math.factorial(k)


def eval_exponential_pdf(lam, x):
    return lam * math.exp(-lam * x)


def make_poisson_pmf(lam, high):
    pmf = Pmf()
    for k in range(0, high + 1):
        p = eval_poisson_pmf(lam, k)
        pmf.set(k, p)
    pmf.normalize()
    return pmf


def make_exponential_pmf(lam, high, n=200):
    pmf = Pmf()
    for x in np.linspace(0, high, n):
        p = eval_exponential_pdf(lam, x)
        pmf.set(x, p)
    pmf.normalize()
    return pmf


def make_goal_pmf(suite):
    meta_pmf = {}
    for lam, prob in suite.iter_items():
        pmf = make_poisson_pmf(lam, 10)
        meta_pmf[pmf] = prob
    mix = make_mixture(meta_pmf)
    return mix


def make_time_pmf(suite):
    meta_pmf = {}
    for lam, prob in suite.iter_items():
        pmf = make_exponential_pmf(lam, high=2, n=201)
        meta_pmf[pmf] = prob
    mix = make_mixture(meta_pmf)
    return mix


def pmf_prob_less(pmf_1, pmf_2):
    total = 0.0
    for v1, p1 in pmf_1.iter_items():
        for v2, p2 in pmf_2.iter_items():
            if v1 < v2:
                total += p1 * p2
    return total
