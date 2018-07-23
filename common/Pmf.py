import random

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
        prob = (100 - percentage) / 2
        return self.percentile(prob), self.percentile(100 - prob)

    def max_likelihood(self):
        return self.d.index[self.d.prob.idxmax()]

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
        self.sort()

        run_sum = 0
        xs = []
        cs = []
        for value, prob in self.iter_items():
            run_sum += prob
            xs.append(value)
            cs.append(run_sum)
        total = float(run_sum)
        ps = [c / total for c in cs]

        name = name if name is not None else self.name
        return common.Cdf.Cdf(xs, ps, name)

    def max(self, k):
        cdf = self.make_cdf()
        cdf.ps = [p ** k for p in cdf.ps]
        return cdf

    def plot(self, legend=False):
        ax = self.d.plot(legend=legend)
        ax.set_xlabel(self.value_desc)
        ax.set_ylabel('Probability')

    def plot_bar(self, legend=False):
        ax = self.d.plot.bar(legend=legend)
        ax.set_xlabel(self.value_desc)
        ax.set_ylabel('Probability')
