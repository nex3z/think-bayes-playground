from common.Suite import Suite


class Price(Suite):
    def __init__(self, pmf, player):
        super().__init__(pmf)
        self.player = player

    def likelihood(self, data, hypo):
        price = hypo
        guess = data
        error = price - guess
        like = self.player.error_density(error)
        return like
