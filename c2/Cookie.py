from common.Pmf import Pmf


class Cookie(Pmf):
    mixes = {
        'Bowl 1': dict(vanilla=0.75, chocolate=0.25),
        'Bowl 2': dict(vanilla=0.5, chocolate=0.5)
    }

    def likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        return mix[data]

    def update(self, data):
        for hypo in self.values():
            like = self.likelihood(data, hypo)
            self.mult(hypo, like)
        self.normalize()
