from common.Pmf import Pmf


class Cookie(Pmf):
    bowl_1 = {'vanilla': 0.75, 'chocolate': 0.25}
    bowl_2 = {'vanilla': 0.5, 'chocolate': 0.5}
    mixes = {'Bowl 1': bowl_1, 'Bowl 2': bowl_2}

    def likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        return mix[data]

    def update(self, data):
        for hypo in self.values():
            like = self.likelihood(data, hypo)
            self.mult(hypo, like)
        self.normalize()
