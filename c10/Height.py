import itertools

from common.Joint import Joint
from common.Suite import Suite
from common.util import eval_gaussian_pdf


class Height(Suite, Joint):
    def __init__(self, mus, sigmas):
        pairs = [(mu, sigma) for (mu, sigma) in itertools.product(mus, sigmas)]
        Suite.__init__(self, pairs)

    def likelihood(self, data, hypo):
        x = data
        mu, sigma = hypo
        like = eval_gaussian_pdf(x, mu, sigma)
        return like
