from common.Pmf import Pmf


class Monty(Pmf):
    def likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1

    def update(self, data):
        for hypo in self.hypos():
            like = self.likelihood(data, hypo)
            self.mult(hypo, like)
        self.normalize()
