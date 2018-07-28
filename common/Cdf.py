import bisect
import random
import matplotlib.pyplot as plt

import common.Pmf


class Cdf(object):
    def __init__(self, xs=None, ps=None, name=None):
        self.xs = [] if xs is None else xs
        self.ps = [] if ps is None else ps
        self.name = name

    def items(self):
        return zip(self.xs, self.ps)

    def prob(self, x):
        if x < self.xs[0]:
            return 0.0
        index = bisect.bisect(self.xs, x)
        return self.ps[index - 1]

    def value(self, p):
        if p < 0 or p > 1:
            raise ValueError('Probability p must be in range [0, 1]')

        if p == 0: return self.xs[0]
        if p == 1: return self.xs[-1]
        index = bisect.bisect(self.ps, p)
        if p == self.ps[index - 1]:
            return self.xs[index - 1]
        else:
            return self.xs[index]

    def random(self):
        return self.value(random.random())

    def sample(self, n):
        return [self.random() for _ in range(n)]

    def make_pmf(self, name=None):
        pmf = common.Pmf.Pmf(name if name is not None else self.name)
        prev = 0.0
        for value, prob in self.items():
            pmf.incr(value, prob - prev)
            prev = prob
        return pmf

    def plot(self):
        plt.figure()
        plt.plot(self.xs, self.ps)
        if self.name is not None:
            plt.title(self.name)
        plt.show()
