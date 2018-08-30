import math
import random

import numpy as np
from common.correlation import least_squares

from common.Cdf import Cdf
from common.util import gaussian_cdf, make_cdf_from_list


def make_cdf(name=""):
    n = 53.0
    freqs = [0, 2, 31, 42, 48, 51, 52, 53]
    ps = [freq / n for freq in freqs]
    xs = np.arange(-1.5, 6.5, 1.0)

    cdf = Cdf(xs, ps, name=name)
    return cdf


def fit_cdf(cdf):
    xs, ps = cdf.values(), cdf.probs()
    cps = [1 - p for p in ps]

    xs = xs[1:-1]
    lcps = [math.log(p) for p in cps[1:-1]]

    _inter, slope = least_squares(xs, lcps)
    return -slope


def generate_cdf(n=1000, pc=0.35, lam1=0.79, lam2=5.0, name=""):
    xs = generate_sample(n, pc, lam1, lam2)
    cdf = make_cdf_from_list(xs, name=name)
    return cdf


def generate_sample(n, pc, lam1, lam2):
    xs = [generate_rdt(pc, lam1, lam2) for _ in range(n)]
    return xs


def generate_rdt(pc, lam1, lam2):
    if random.random() < pc:
        return -random.expovariate(lam2)
    else:
        return random.expovariate(lam1)


def volume(diameter, factor=4*math.pi/3):
    return factor * (diameter / 2.0) ** 3


def diameter(volume, factor=3/math.pi/4, exp=1/3.0):
    return 2 * (factor * volume) ** exp


def cm_to_bucket(x, factor=10):
    return round(factor * math.log(x))


def uncorrelated_generator(cdf):
    while True:
        x = cdf.random()
        yield x


def correlated_generator(cdf, rho):
    def transform(x):
        p = gaussian_cdf(x)
        y = cdf.value(p)
        return y

    x = random.gauss(0, 1)
    yield transform(x)

    sigma = math.sqrt(1 - rho**2)
    while True:
        x = random.gauss(x * rho, sigma)
        yield transform(x)


def rdt_generator(cdf, rho):
    if rho <= 0:
        return uncorrelated_generator(cdf)
    else:
        return correlated_generator(cdf, rho)
