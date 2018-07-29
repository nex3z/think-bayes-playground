from common.Pmf import Pmf
from common.exception import UnimplementedMethodException


class Pdf(object):
    def density(self, x):
        raise UnimplementedMethodException()

    def make_pmf(self, xs, name=''):
        pmf = Pmf(name=name)
        for x in xs:
            pmf.set(x, self.density(x))
        pmf.normalize()
        return pmf
