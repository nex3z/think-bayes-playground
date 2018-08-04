import matplotlib.pyplot as plt
from c8.ElapsedTimeEstimator import ElapsedTimeEstimator
import common.util as util


class WaitMixtureEstimator(object):
    def __init__(self, wtc, are, num_passengers=15):
        self.meta_pmf = {}
        for lam, prob in are.post_lam.iter_items():
            if prob <= 0:
                continue
            ete = ElapsedTimeEstimator(wtc, lam, num_passengers)
            self.meta_pmf[ete.pmf_y] = prob
        self.mixture = util.make_mixture(self.meta_pmf)

    def plot(self):
        plt.figure(figsize=(10, 6))
        for pmf in self.meta_pmf.keys():
            cdf = pmf.make_cdf()
            plt.plot(cdf.xs, cdf.ps, color='b')
        mix_cdf = self.mixture.make_cdf()
        plt.plot(mix_cdf.xs, mix_cdf.ps, color='r')
        plt.show()
