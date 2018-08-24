import matplotlib.pyplot as plt
from c8.ElapsedTimeEstimator import ElapsedTimeEstimator
from common.util import make_mixture
from common.Pmf import Pmf


class WaitMixtureEstimator(object):
    def __init__(self, wtc, are, num_passengers=15):
        self.meta_pmf = Pmf()
        for lam, prob in are.post_lam.iter_items():
            if prob <= 0:
                continue
            ete = ElapsedTimeEstimator(wtc, lam, num_passengers)
            self.meta_pmf.set(ete.pmf_y, prob)
        self.mixture = make_mixture(self.meta_pmf)

    def plot(self, time_limit=600):
        plt.figure(figsize=(8, 6))

        mix_cdf = self.mixture.make_cdf()
        mix_cdf.d = mix_cdf.d.loc[mix_cdf.d.value <= time_limit, ]
        plt.plot(mix_cdf.d.value, mix_cdf.d.prob, color='r')

        for pmf in self.meta_pmf.values():
            cdf = pmf.make_cdf()
            cdf.d = cdf.d.loc[cdf.d.value <= time_limit, ]
            plt.plot(cdf.d.value, cdf.d.prob, color='b')

        plt.show()
