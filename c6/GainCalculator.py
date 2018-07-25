import numpy as np


class GainCalculator(object):
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def expected_gains(self, low=0, high=75000, n=101):
        bids = np.linspace(low, high, n)
        gains = [self.expected_gain(bid) for bid in bids]
        return bids, gains

    def expected_gain(self, bid):
        suite = self.player.posterior
        total = 0
        for price, prob in suite.iter_items():
            gain = self.gain(bid, price)
            total += prob * gain
        return total

    def gain(self, bid, price):
        if bid > price:
            return 0

        diff = price - bid
        prob = self.prob_win(diff)

        if diff <= 250:
            return 2 * price * prob
        else:
            return price * prob

    def prob_win(self, diff):
        prob = self.opponent.prob_overbid() + self.opponent.prob_worse_than(diff)
        return prob
