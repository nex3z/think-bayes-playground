import scipy.special
from common.Cdf import Cdf
from common.Pmf import Pmf


class Beta(object):
    def __init__(self, alpha=1, beta=1, name=''):
        self.alpha = alpha
        self.beta = beta
        self.name = name

    def update(self, data):
        heads, tails = data
        self.alpha += heads
        self.beta += tails

    def mean(self):
        return float(self.alpha) / (self.alpha + self.beta)

    def eval_pdf(self, x):
        return x ** (self.alpha - 1) * (1 - x) ** (self.beta - 1)

    def make_pmf(self, steps=101, name=''):
        name = name if name else self.name
        if self.alpha < 1 or self.beta < 1:
            cdf = self.make_cdf()
            pmf = cdf.make_pmf(name)
            return pmf

        xs = [i / (steps - 1.0) for i in range(steps)]
        probs = [self.eval_pdf(x) for x in xs]
        pmf = Pmf(values=xs, probs=probs, name=name)
        return pmf

    def make_cdf(self, steps=101):
        xs = [i / (steps - 1.0) for i in range(steps)]
        ps = [scipy.special.betainc(self.alpha, self.beta, x) for x in xs]
        cdf = Cdf(xs, ps)
        return cdf

    def summary(self):
        pmf = self.make_pmf()
        cdf = self.make_cdf()
        print("Maximum likelihood: {}".format(pmf.max_likelihood()))
        print("Mean: {}".format(self.mean()))
        print("Median: {}".format(cdf.percentile(50)))
        print("Credible Interval (90%): {}".format(cdf.credible_interval(90)))
        print("P(x = 50%) = {}".format(pmf.prob(50)))

    def plot(self):
        self.make_pmf().plot()
