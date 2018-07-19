from common.Suite import Suite


class Train(Suite):
    def __init__(self, values=None, prob_dist=lambda hypos: [1.0 / len(hypos) for _ in hypos]):
        super().__init__(values, hypo_desc='Train number')
        probs = prob_dist(values)
        for hypo, prob in zip(self.hypos(), probs):
            self.set(hypo, prob)
        self.normalize()

    def likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0 / hypo
