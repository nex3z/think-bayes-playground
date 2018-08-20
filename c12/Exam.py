from c12.util import *
from common.Pmf import Pmf
from common.util import make_mixture


class Exam(object):
    def __init__(self):
        self.scale = read_scale()

        scores = read_ranks()
        self.pmf_score = Pmf(values=scores.score, probs=scores.number)

        self.raw = self.reverse_scale(self.pmf_score)
        self.max_score = max(self.raw.values())
        self.prior = divide_values(self.raw, self.max_score)

        self.difficulties = make_difficulties(center=-0.05, width=1.8, n=self.max_score)

    def reverse(self, score):
        raw = self.scale.reverse(score)
        return max(raw, 0)

    def reverse_scale(self, pmf):
        reverse = Pmf()
        for value, prob in pmf.iter_items():
            raw = self.reverse(value)
            reverse.incr(raw, prob)
        return reverse

    def make_p_correct_cdf(self):
        pmf = self.prior.copy()
        pmf.sort_by_value()
        return pmf.make_cdf('p_correct')

    def make_raw_score_dist(self, efficacies):
        pmfs = Pmf()
        for efficacy, prob in efficacies.iter_items():
            print("make_raw_score_dist(): processing {} {}".format(efficacy, prob))
            scores = pmf_correct(efficacy, self.difficulties)
            pmfs.set(scores, prob)
        mix = make_mixture(pmfs)
        return mix


def divide_values(pmf, denom):
    pmf = pmf.copy()
    pmf.d.value = pmf.d.value / denom
    return pmf
