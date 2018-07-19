from common.Suite import Suite


class Dice(Suite):
    def likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0 / hypo
