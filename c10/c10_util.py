import math
import pickle

import numpy as np

from common.Pmf import Pmf


def load_height(path='./variability_data_1000.pkl'):
    with open(path, 'rb') as f:
        data = pickle.load(f)
        xs_male = np.array(data[1])
        xs_female = np.array(data[2])
    return xs_male, xs_female


def jitter(values, jitter=0.5):
    noise = np.random.uniform(-jitter, jitter, len(values))
    return values + noise


def find_prior_ranges(xs, num_points=31, num_stderrs=3.0):
    def make_range(estimate, stderr):
        spread = stderr * num_stderrs
        array = np.linspace(estimate - spread, estimate + spread, num_points)
        return array

    n = len(xs)
    m = np.mean(xs)
    s = np.std(xs)

    stderr_m = s / math.sqrt(n)
    mus = make_range(m, stderr_m)

    stderr_s = s / math.sqrt(2 * (n - 1))
    sigmas = make_range(s, stderr_s)

    return mus, sigmas


def coef_variation(suite):
    pmf = Pmf()
    for (mu, sigma), p in suite.iter_items():
        pmf.incr(sigma/mu, p)
    return pmf
