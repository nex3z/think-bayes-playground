from common.Pmf import Pmf


class Joint(Pmf):
    def marginal(self, i, name=''):
        pmf = Pmf(name=name)
        for vs, prob in self.iter_items():
            pmf.incr(vs[i], prob)
        return pmf

    def conditional(self, i, j, val, name=''):
        pmf = Pmf(name=name)
        for vs, prob in self.iter_items():
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
        for value, prob in df_prob.itertuples(index=False):
            interval.append(value)
            total += prob
            if total >= percentage / 100.0:
                break
        return interval
