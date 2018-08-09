from common.Pmf import Pmf
from common.exception import UnimplementedMethodException


class Pdf(object):
    def density(self, x):
        raise UnimplementedMethodException()

    def make_pmf(self, xs, name=''):
        probs = self.density(xs)
        pmf = Pmf(values=xs, probs=probs, name=name)
        return pmf
