import itertools
import math

import numpy as np
import pandas as pd

from common.Interpolator import Interpolator
from common.Pmf import Pmf


def read_scale(file='./c12/data/sat_scale.csv'):
    df_data = pd.read_csv(file, skiprows=1)
    df_select = df_data.loc[:, [df_data.columns[2], df_data.columns[3]]].dropna()
    df_select.columns = ['score', 'scaled']

    df_select.scaled = df_select.scaled.map(parse_scale_raw)
    df_select.score = df_select.score.astype(int)
    df_select.scaled = df_select.scaled.astype(int)
    df_select.sort_values(by='score', inplace=True)
    df_select.reset_index(drop=True, inplace=True)

    return Interpolator(df_select.score, df_select.scaled)


def read_ranks(file='./c12/data/sat_ranks.csv'):
    df_data = pd.read_csv(file, skiprows=2)
    df_select = df_data.loc[:, [df_data.columns[0], df_data.columns[1]]].dropna()
    df_select.columns = ['score', 'number']

    df_select.score = df_select.score.astype(int)
    df_select.number = df_select.number.astype(int)

    return df_select


def parse_scale_raw(raw):
    split = [int(x) for x in raw.split('-')]
    return sum(split) / len(split)


def pmf_prob_greater(pmf1, pmf2):
    total = 0.0
    for (v1, p1), (v2, p2) in itertools.product(pmf1.iter_items(), pmf2.iter_items()):
        if v1 > v2:
            total += p1 * p2
    return total


def pmf_prob_equal(pmf1, pmf2):
    total = 0.0
    for (v1, p1), (v2, p2) in itertools.product(pmf1.iter_items(), pmf2.iter_items()):
        if v1 == v2:
            total += p1 * p2
    return total


def pmf_prob_less(pmf1, pmf2):
    total = 0.0
    for (v1, p1), (v2, p2) in itertools.product(pmf1.iter_items(), pmf2.iter_items()):
        if v1 < v2:
            total += p1 * p2
    return total


def make_difficulties(center, width, n):
    low, high = center - width, center + width
    return np.linspace(low, high, n)


def prob_correct(efficacy, difficulty, a=1):
    return 1 / (1 + math.exp(-a * (efficacy - difficulty)))


def pmf_correct(efficacy, difficulties):
    pmf0 = Pmf([0])
    ps = [prob_correct(efficacy, diff) for diff in difficulties]
    pmfs = [binary_pmf(p) for p in ps]
    dist = sum(pmfs, pmf0)
    return dist


def binary_pmf(p):
    pmf = Pmf()
    pmf.set(1, p)
    pmf.set(0, 1 - p)
    return pmf
