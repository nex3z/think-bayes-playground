from common.Suite import Suite
from common.util import eval_binomial_pmf


class Sat(Suite):
    def __init__(self, exam, score):
        super().__init__(values=exam.prior.d.value, probs=exam.prior.d.prob)
        self.exam = exam
        self.score = score
        self.update(score)

    def likelihood(self, data, hypo):
        p_correct = hypo
        score = data

        k = self.exam.reverse(score)
        n = self.exam.max_score
        like = eval_binomial_pmf(k, n, p_correct)
        return like
