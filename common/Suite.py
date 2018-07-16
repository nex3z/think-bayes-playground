from common.Pmf import Pmf
from common.exception import UnimplementedMethodException


class Suite(Pmf):
    def likelihood(self, data, hypo):
        raise UnimplementedMethodException()

    def update(self, data):
        for hypo in self.hypos():
            like = self.likelihood(data, hypo)
            self.mult(hypo, like)
        return self.normalize()

    def update_set(self, dataset):
        for data in dataset:
            for hypo in self.hypos():
                like = self.likelihood(data, hypo)
                self.mult(hypo, like)
        return self.normalize()
