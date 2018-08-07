from common.Suite import Suite
from common.util import eval_poisson_pmf


class Elapsed(Suite):
    def likelihood(self, data, hypo):
        x = hypo
        lam, k = data
        like = eval_poisson_pmf(lam * x, k)
        return like
