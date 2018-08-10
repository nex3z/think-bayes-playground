from common.Suite import Suite


class Train(Suite):
    def __init__(self, values=None, dist=lambda hypos: [1.0 / len(hypos) for _ in hypos]):
        super().__init__(values=values, probs=dist(values), value_desc='Train number')

    def likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0 / hypo
