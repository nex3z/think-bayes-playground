from common.Suite import Suite


class Euro(Suite):
    def __init__(self, values=None):
        super().__init__(values, value_desc='x')

    def likelihood(self, data, hypo):
        if data == 'H':
            return hypo / 100.0
        else:
            return 1 - hypo / 100.0

    def summary(self):
        cdf = self.make_cdf()
        print("Maximum likelihood: {}".format(self.max_likelihood()))
        print("Mean: {}".format(self.mean()))
        print("Median: {}".format(cdf.percentile(50)))
        print("Credible Interval: {}".format(cdf.credible_interval()))
        print("P(x = 50%) = {}".format(self.prob(50)))
