from common.Suite import Suite
from c12.util import *


class TopLevel(Suite):
    def __init__(self):
        super().__init__(values=['A', 'B'])

    def update(self, data):
        sat_a, sat_b = data
        like_a = pmf_prob_greater(sat_a, sat_b)
        like_b = pmf_prob_less(sat_a, sat_b)
        like_c = pmf_prob_equal(sat_a, sat_b)

        like_a += like_c / 2.0
        like_b += like_c / 2.0

        self.mult('A', like_a)
        self.mult('B', like_b)
        self.normalize()
