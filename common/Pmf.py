import random

import matplotlib.pyplot as plt

import common.Cdf
from common.DfWrapper import DfWrapper


class Pmf(DfWrapper):
    def __init__(self, values=None, name='', value_desc=''):
        super().__init__(values, name)
        self.value_desc = value_desc

    def __add__(self, other):
        pmf = Pmf()
        for v1, p1 in self.iter_items():
            for v2, p2 in other.iter_items():
                pmf.incr(v1 + v2, p1 * p2)
        return pmf

    def __sub__(self, other):
        pmf = Pmf()
        for v1, p1 in self.iter_items():
            for v2, p2 in other.iter_items():
                pmf.incr(v1 - v2, p1 * p2)
        return pmf

    def prob(self, x, default=0):
        return super(Pmf, self).get(x, default)

    def probs(self, xs):
        return [self.prob(x) for x in xs]

    def prob_greater(self, x):
        return self.d.loc[self.d.index > x, 'prob'].sum()

    def prob_less(self, x):
        return self.d.loc[self.d.index < x, 'prob'].sum()

    def top(self, n=5):
        df_sort = self.d.sort_values('prob', ascending=False)
        return df_sort.head(n)

    def mean(self):
        return (self.d.index * self.d.prob).sum()

    def percentile(self, percentage):
        p = percentage / 100.0
        total = 0
        for value, prob in self.iter_items():
            total += prob
            if total >= p:
                return value

    def credible_interval(self, percentage=90):
        cdf = self.make_cdf()
        return cdf.credible_interval(percentage)

    def max_likelihood(self):
        return self.d.prob.idxmax()

    def random(self):
        if self.is_empty():
            raise ValueError("PMF is empty.")

        target = random.random()
        total = 0.0
        for value, prob in self.iter_items():
            total += prob
            if total >= target:
                return value

        assert False

    def make_cdf(self, name=None):
        df_cdf = self.d.copy()
        df_cdf.sort_index(inplace=True)
        name = name if name is not None else self.name
        return common.Cdf.Cdf(df_cdf.index, df_cdf.prob.cumsum(), name, self.value_desc)

    def print(self):
        print(self.d)

    def plot(self, legend=False):
        ax = self.d.plot(legend=legend)
        ax.set_xlabel(self.value_desc)
        ax.set_ylabel('Probability')

    def plot_with(self, pmfs):
        plt.figure()
        plt.plot(self.d.index, self.d.prob, label=self.name)
        for pmf in pmfs:
            plt.plot(pmf.d.prob, label=pmf.name)
        plt.legend()
        plt.show()

    def plot_bar(self, legend=False):
        ax = self.d.plot.bar(legend=legend)
        ax.set_xlabel(self.value_desc)
        ax.set_ylabel('Probability')
