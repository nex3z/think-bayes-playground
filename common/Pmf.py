from common.DfWrapper import DfWrapper


class Pmf(DfWrapper):
    def prob(self, event, default=0):
        return super(Pmf, self).get(event, default)

    def probs(self, events):
        return [self.prob(key) for key in events]
