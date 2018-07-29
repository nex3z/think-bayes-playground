import pandas as pd

import common.Pmf
import common.Pmf
import copy


class DfWrapper(object):
    def __init__(self, values=None, name=''):
        self.name = name
        self.d = pd.DataFrame(columns=['prob'])
        self.d.prob = self.d.prob.astype(float)
        self.d.index.name = 'value'

        if values is None:
            return

        if isinstance(values, dict):
            self.__init_map(values)
        elif isinstance(values, common.Pmf.Pmf):
            self.__init_pmf(values)
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

    def __init_pmf(self, pmf):
        for value, prob in pmf.iter_items():
            self.set(value, prob)

    def __init_sequence(self, values):
        for value in values:
            self.set(value, 1.0)

    def __init_map(self, mapping):
        for value, prob in mapping.items():
            self.set(value, prob)

    def __init_failure(self, values):
        raise ValueError('Initialization failed')

    def iter_items(self):
        return self.d.prob.iteritems()

    def values(self):
        return self.d.index.values

    def set(self, value, prob):
        self.d.loc[value] = prob

    def get(self, value, default=0):
        return self.d.prob.get(value, default)

    def mult(self, value, factor):
        self.d.loc[value] = self.d.loc[value] * factor

    def incr(self, value, term=1):
        if value in self.d.index:
            self.d.loc[value] = self.d.loc[value] + term
        else:
            self.set(value, term)
            self.sort()

    def sort(self):
        self.d.sort_index(inplace=True)

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

    def is_empty(self):
        return len(self.d) == 0

    def copy(self, name=None):
        new = copy.copy(self)
        new.d = self.d.copy()
        new.name = name if name is not None else self.name
        return new

    # def __iter__(self):
    #     return self.d.iterrows()
