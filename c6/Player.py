import matplotlib.pyplot as plt
import numpy as np

from c6.GainCalculator import GainCalculator
from c6.Price import Price
from common.util import make_cdf_from_list
from common.EstimatedPdf import EstimatedPdf
from common.GaussianPdf import GaussianPdf


class Player(object):
    def __init__(self, prices, bids, diffs):
        self.pdf_price = EstimatedPdf(prices)
        self.cdf_diff = make_cdf_from_list(diffs)
        self.pdf_error = GaussianPdf(mu=0, sigma=np.std(diffs))
        self.prior = None
        self.posterior = None

    def error_density(self, error):
        return self.pdf_error.density(error)

    def make_beliefs(self, guess):
        pmf = self.pmf_price()
        self.prior = Price(pmf, self)
        self.posterior = self.prior.copy()
        self.posterior.update(guess)

    n = 101
    price_xs = np.linspace(0, 75000, n)

    def pmf_price(self):
        return self.pdf_price.make_pmf(self.price_xs)

    def prob_overbid(self):
        return self.cdf_diff.prob(-1)

    def prob_worse_than(self, diff):
        return 1 - self.cdf_diff.prob(diff)

    def calc_bid_gain(self, guess, opponent):
        self.make_beliefs(guess)
        calc = GainCalculator(self, opponent)
        return calc.expected_gains()

    def optimal_bid(self, guess, opponent):
        self.make_beliefs(guess)
        calc = GainCalculator(self, opponent)
        bids, gains = calc.expected_gains()
        gain, bid = max(zip(gains, bids))
        return bid, gain

    def plot(self):
        plt.figure()
        if self.prior is not None:
            plt.plot(self.prior.d, label="prior")
        if self.posterior is not None:
            plt.plot(self.posterior.d, label="posterior")
        plt.legend()
