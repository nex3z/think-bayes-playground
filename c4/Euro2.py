from common.Suite import Suite


class Euro(Suite):
    def __init__(self, values=None):
        super().__init__(values, value_desc='x')

    def likelihood(self, data, hypo):
        x = hypo / 100.0
        heads, tails = data
        return x**heads * (1 - x)**tails

    def summary(self):
        cdf = self.make_cdf()
        print("Maximum likelihood: {}".format(self.max_likelihood()))
        print("Mean: {}".format(self.mean()))
        print("Median: {}".format(cdf.percentile(50)))
        print("Credible Interval (90%): {}".format(cdf.credible_interval(90)))
        print("P(x = 50%) = {}".format(self.prob(50)))
