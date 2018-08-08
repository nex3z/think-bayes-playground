from common.Pmf import Pmf
from common.exception import UnimplementedMethodException


class Suite(Pmf):
    def likelihood(self, data, hypo):
        raise UnimplementedMethodException()

    def update(self, data):
        likelihoods = [self.likelihood(data, hypo) for hypo in self.values()]
        self.mult(factor=likelihoods)
        return self.normalize()

    def update_set(self, dataset):
        for data in dataset:
            likelihoods = [self.likelihood(data, hypo) for hypo in self.values()]
            self.mult(factor=likelihoods)
        return self.normalize()
