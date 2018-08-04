from common.Suite import Suite
import common.util as util


class ArrivalRate(Suite):
    def likelihood(self, data, hypo):
        lam = hypo
        y, k = data
        like = util.eval_poisson_pmf(lam * y, k)
        return like
