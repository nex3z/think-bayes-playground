import copy

import numpy as np
import pandas as pd


class DfWrapper(object):
    def __init__(self, values=None, probs=None, name=''):
        self.name = name
        self.d = pd.DataFrame(columns=['value', 'prob'])
        self.d.prob = self.d.prob.astype(float)

        if values is None:
            return

        if probs is not None:
            self.__init_value_prob(values, probs)
        elif isinstance(values, dict):
            self.__init_map(values)
        elif isinstance(values, DfWrapper):
            self.__init_df_wrapper(values)
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

    def __init_value_prob(self, values, probs):
        self.d.value = values
        self.d.prob = probs

    def __init_map(self, mapping):
        for value, prob in mapping.items():
            self.set(value, prob)

    def __init_df_wrapper(self, df_wrapper):
        self.d = df_wrapper.d.copy()

    def __init_sequence(self, values):
        self.d.value = values
        self.d.prob = 1.0

    def __init_failure(self, values):
        raise ValueError('Initialization failed')

    def iter_items(self):
        return self.d.itertuples(index=False)

    def values(self):
        return self.d.value.values

    def set(self, value, prob):
        select = self.d.value == value
        if any(select):
            self.d.prob[select] = prob
        else:
            self.d = self.d.append({'value': value, 'prob': prob}, ignore_index=True)

    def get(self, value, default=0):
        result = self.d.loc[self.d.value == value, 'prob']
        return result.values[0] if len(result) > 0 else default

    def mult(self, value=np.nan, factor=1.0):
        if pd.isna(value):
            self.d.prob = self.d.prob * factor
        else:
            select = self.d.value == value
            self.d.loc[select, 'prob'] = self.d.loc[select, 'prob'] * factor

    def incr(self, value, term=1):
        select = self.d.value == value
        if any(select):
            self.d.loc[select, 'prob'] = self.d.loc[select, 'prob'] + term
        else:
            self.d = self.d.append({'value': value, 'prob': term}, ignore_index=True)

    def sort_by_value(self):
        self.d.sort_values(by='value', inplace=True)

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

    def print(self, float_format='%.6g'):
        print(self.d.to_csv(sep='\t', float_format=float_format, index=False))

    def is_empty(self):
        return len(self.d) == 0

    def copy(self, name=None):
        new = copy.copy(self)
        new.d = self.d.copy()
        new.name = name if name is not None else self.name
        return new
