from common.Suite import Suite
from common.util import make_poisson_pmf, eval_binomial_pmf


class Detector(Suite):
    def __init__(self, r, f, high=500, step=1):
        pmf = make_poisson_pmf(r, high, step=step)
        super().__init__(pmf, name=str(r))
        self.r = r
        self.f = f

    def likelihood(self, data, hypo):
        k = data
        n = hypo
        p = self.f
        return eval_binomial_pmf(k, n, p)
