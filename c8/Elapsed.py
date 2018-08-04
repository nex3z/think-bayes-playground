from common.Suite import Suite
import common.util as util


class Elapsed(Suite):
    def likelihood(self, data, hypo):
        x = hypo
        lam, k = data
        like = util.eval_poisson_pmf(lam * x, k)
        return like
