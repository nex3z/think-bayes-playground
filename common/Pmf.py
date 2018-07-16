from common.DfWrapper import DfWrapper


class Pmf(DfWrapper):
    def __init__(self, values=None, name='', hypo_desc=''):
        super().__init__(values, name)
        self.hypo_desc = hypo_desc

    def prob(self, event, default=0):
        return super(Pmf, self).get(event, default)

    def probs(self, events):
        return [self.prob(key) for key in events]

    def plot(self, legend=False):
        ax = self.d.plot(legend=legend)
        ax.set_xlabel(self.hypo_desc)
        ax.set_ylabel('Probability')

    def mean(self):
        return (self.d.index * self.d.prob).sum()

    def percentile(self, percentage):
        p = percentage / 100.0
        total = 0
        for hypo, prob in self.iter_items():
            total += prob
            if total >= p:
                return hypo

    def credible_interval(self, percentage=90):
        prob = (100 - percentage) / 2
        return self.percentile(prob), self.percentile(100 - prob)

    def max_likelihood(self):
        return self.d.index[self.d.prob.idxmax()]
