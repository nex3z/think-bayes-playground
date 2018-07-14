from common.DictWrapper import DictWrapper


class Pmf(DictWrapper):
    def prob(self, key, default=0):
        return self.d.get(key, default)

    def probs(self, keys):
        return [self.prob(key) for key in keys]

    def normalize(self, fraction=1.0):
        total = self.total()
        if total <= 0:
            raise ValueError('Total probability is zero.')

        factor = float(fraction) / total
        for x in self.d.keys():
            self.d[x] *= factor
        return total
