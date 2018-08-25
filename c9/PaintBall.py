from c9.c9_util import make_location_pmf
from common.Joint import Joint
from common.Suite import Suite


class PaintBall(Suite, Joint):
    def __init__(self, alphas, betas, locations):
        self.locations = locations
        pairs = [(alpha, beta) for alpha in alphas for beta in betas]
        Suite.__init__(self, pairs)

    def likelihood(self, data, hypo):
        alpha, beta = hypo
        x = data
        pmf = make_location_pmf(alpha, beta, self.locations)
        like = pmf.prob(x)
        return like
