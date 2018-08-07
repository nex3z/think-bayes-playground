from common.Suite import Suite
from common.util import eval_poisson_pmf


class ArrivalRate(Suite):
    def likelihood(self, data, hypo):
        lam = hypo
        y, k = data
        like = eval_poisson_pmf(lam * y, k)
        return like
