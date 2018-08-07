import numpy as np
from c8.ArrivalRate import ArrivalRate


class ArrivalRateEstimator(object):
    def __init__(self, passenger_data):
        low, high = 0, 5
        n = 51
        hypos = np.linspace(low, high, n) / 60

        self.prior_lam = ArrivalRate(hypos)
        self.post_lam = self.prior_lam.copy()
        for k1, y, k2 in passenger_data:
            self.post_lam.update((y, k2))

    def plot(self):
        cdf_prior = self.prior_lam.make_cdf('prior')
        cdf_prior.d.index = cdf_prior.d.index * 60
        cdf_post = self.post_lam.make_cdf('posterior')
        cdf_post.d.index = cdf_post.d.index * 60
        cdf_prior.plot_with([cdf_post])
