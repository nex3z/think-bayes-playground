from common.Pmf import Pmf
from ast import literal_eval as make_tuple


class Joint(Pmf):
    def marginal(self, i, name=''):
        pmf = Pmf(name=name)
        for vs, prob in self.iter_items():
            vs = make_tuple(vs)
            pmf.incr(vs[i], prob)
        return pmf

    def conditional(self, i, j, val, name=''):
        pmf = Pmf(name=name)
        for vs, prob in self.iter_items():
            vs = make_tuple(vs)
            if vs[j] != val:
                continue
            pmf.incr(vs[i], prob)
        pmf.normalize()
        return pmf

    def max_like_interval(self, percentage=90):
        df_prob = self.d.copy()
        df_prob.sort_values(by=['prob'], ascending=False, inplace=True)

        interval = []
        total = 0
        for idx, row in df_prob.iterrows():
            interval.append(make_tuple(idx))
            total += row.prob
            if total >= percentage / 100.0:
                break
        return interval
