import itertools
import math

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

from common.Joint import Joint
from common.Pmf import Pmf
from common.Suite import Suite
from common.util import eval_gaussian_pdf, eval_gaussian_log_pdf, median_s


class Height(Suite, Joint):
    def __init__(self, mus, sigmas, name=''):
        pairs = [(mu, sigma) for (mu, sigma) in itertools.product(mus, sigmas)]
        Suite.__init__(self, pairs, name=name)

    def likelihood(self, data, hypo):
        x = data
        mu, sigma = hypo
        like = eval_gaussian_pdf(x, mu, sigma)
        return like

    def log_likelihood(self, data, hypo):
        x = data
        mu, sigma = hypo
        log_like = scipy.stats.norm.logpdf(x, mu, sigma)
        return log_like

    def log_update_set_abc(self, n, m, s):
        for hypo in sorted(self.values()):
            mu, sigma = hypo

            stderr_m = sigma / math.sqrt(n)
            loglike = eval_gaussian_log_pdf(m, mu, stderr_m)

            stderr_s = sigma / math.sqrt(2 * (n - 1))
            loglike += eval_gaussian_log_pdf(s, sigma, stderr_s)

            self.incr(hypo, loglike)

    def log_update_set_mean_var(self, dataset):
        xs = dataset
        n = len(xs)
        m = np.mean(xs)
        s = np.std(xs)
        self.log_update_set_abc(n, m, s)

    def log_update_set_median_ipr(self, dataset):
        xs = dataset
        n = len(xs)
        median, s = median_s(xs, 1)
        self.log_update_set_abc(n, median, s)

    def make_cv_cdf(self, name=''):
        mean = np.array([self.d.value[i][0] for i in range(len(self.d))])
        std = np.array([self.d.value[i][1] for i in range(len(self.d))])
        cv = std / mean
        pmf = Pmf(values=cv, probs=self.d.prob, name=self.name if self.name else name)
        pmf.sort_by_value()
        return pmf.make_cdf()

    def plot(self):
        xs = np.array(sorted(set([self.d.value[i][0] for i in range(len(self.d))])))
        ys = np.array(sorted(set([self.d.value[i][1] for i in range(len(self.d))])))
        X, Y = np.meshgrid(xs, ys)
        Z = np.zeros(X.shape)
        for i in range(len(xs)):
            for j in range(len(ys)):
                Z[i, j] = self.d.prob.loc[self.d.value == (xs[i], ys[j]), ].values[0]
        fig, ax = plt.subplots()
        cs = plt.contourf(X, Y, Z, cmap=plt.cm.Blues, antialiased=False)
        ax.set_xlabel('Average height(CM)')
        ax.set_ylabel('Standard deviation(CM)')
        plt.colorbar(cs)
        # plt.clabel(cs)
        plt.show()
