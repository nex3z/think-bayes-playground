import random

import matplotlib.pyplot as plt
import pandas as pd

import common.Pmf
from common.DfWrapper import DfWrapper


class Cdf(DfWrapper):
    def __init__(self, xs=None, ps=None, name='', value_desc=''):
        super().__init__(name=name)
        self.value_desc = value_desc

        xs = [] if xs is None else xs
        ps = [] if ps is None else ps
        self.d = pd.DataFrame({'value': xs, 'prob': ps})

    def prob(self, x):
        if x < self.d.value.iat[0]:
            return 0.0
        pos = self.d.value.searchsorted(x)[0]
        return self.d.prob.iat[pos - 1]

    def value(self, p):
        if p < 0 or p > 1:
            raise ValueError('Probability p must be in range [0, 1]')
        elif p == 0:
            return self.d.value.iat[0]
        elif p == 1:
            return self.d.value.iat[-1]
        else:
            pos = self.d.prob.searchsorted(p)[0]
            if p == self.d.prob.iat[pos - 1]:
                return self.d.value.iat[pos - 1]
            else:
                return self.d.value.iat[pos]

    def percentile(self, p):
        return self.value(p / 100.0)

    def credible_interval(self, percentage=90):
        prob = (1 - percentage / 100.0) / 2
        interval = self.value(prob), self.value(1 - prob)
        return interval

    def max(self, k):
        cdf = self.copy()
        cdf.d.prob = self.d.prob ** k
        return cdf

    def make_pmf(self, name=None):
        name = name if name is not None else self.name
        pmf = common.Pmf.Pmf(name=name)
        prev = 0.0
        for value, prob in self.iter_items():
            pmf.incr(value, prob - prev)
            prev = prob
        return pmf

    def random(self):
        return self.value(random.random())

    def sample(self, n):
        return [self.random() for _ in range(n)]

    def plot(self):
        fig, ax = plt.subplots()
        plt.plot(self.d.value, self.d.prob)
        ax.set_xlabel(self.value_desc)
        ax.set_ylabel('Probability')

    def plot_with(self, cdfs):
        plt.figure()
        plt.plot(self.d.value, self.d.prob, label=self.name)
        for cdf in cdfs:
            plt.plot(cdf.d.value, cdf.d.prob, label=cdf.name)
        plt.legend()
        plt.show()

