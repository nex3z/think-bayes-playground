from common.Suite import Suite


class Euro(Suite):
    def __init__(self, values=None):
        super().__init__(values, hypo_desc='x')

    def likelihood(self, data, hypo):
        x = hypo / 100.0
        heads, tails = data
        return x**heads * (1 - x)**tails

    def summary(self):
        print("Maximum likelihood: {}".format(self.max_likelihood()))
        print("Mean: {}".format(self.mean()))
        print("Median: {}".format(self.percentile(50)))
        print("Credible Interval: {}".format(self.credible_interval()))
        print("P(x = 50%) = {}".format(self.prob(50)))
