from common.Suite import Suite
from common.util import make_gaussian_pmf, eval_poisson_pmf


class Hockey(Suite):
    def __init__(self, name=''):
        pmf = make_gaussian_pmf(mu=2.7, sigma=0.3, num_sigmas=4)
        super().__init__(pmf, name=name)

    def likelihood(self, data, hypo):
        lam = hypo
        k = data
        like = eval_poisson_pmf(lam, k)
        return like
