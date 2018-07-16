import numpy as np
import pandas as pd


class DfWrapper(object):
    def __init__(self, values=None, name=''):
        self.name = name
        self.d = pd.DataFrame(columns=['prob'])
        self.d.prob = self.d.prob.astype(float)
        self.d.index.name = 'hypo'

        if values is None:
            return

        if isinstance(values, dict):
            self.__init_map(values)
        else:
            init_methods = [self.__init_sequence, self.__init_failure]
            for method in init_methods:
                try:
                    method(values)
                    break
                except AttributeError:
                    continue

        if len(self.d) > 0:
            self.normalize()

    def __init_sequence(self, hypos):
        for hypo in hypos:
            self.set(hypo, 1.0)

    def __init_map(self, mapping):
        for hypo, prob in mapping.items():
            self.set(hypo, prob)

    def __init_failure(self, values):
        raise ValueError('Initialization failed')

    def iter_items(self):
        return self.d.prob.iteritems()

    def hypos(self):
        return self.d.index.values

    def set(self, hypo, prob):
        self.d.loc[hypo] = prob

    def get(self, hypo, default=0):
        return self.d.prob.get(hypo, default)

    def mult(self, hypo, factor):
        self.d.loc[hypo] = self.d.loc[hypo] * factor

    def total(self):
        total = self.d.prob.sum()
        return 0 if not total else total

    def normalize(self, fraction=1.0):
        total = self.total()
        if total <= 0:
            raise ValueError('Total probability is zero.')

        factor = float(fraction) / total
        self.d.prob *= factor
        return total

    def print(self):
        print(self.d)
