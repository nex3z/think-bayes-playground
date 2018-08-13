from common.Pmf import Pmf
from common.exception import UnimplementedMethodException


class Suite(Pmf):
    def likelihood(self, data, hypo):
        raise UnimplementedMethodException()

    def log_likelihood(self, data, hypo):
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

    def log_update(self, data):
        log_likelihoods = [self.log_likelihood(data, hypo) for hypo in self.values()]
        self.d.prob = self.d.prob + log_likelihoods
        # for hypo in self.values():
        #     like = self.log_likelihood(data, hypo)
        #     self.incr(hypo, like)

    def log_update_set(self, dataset):
        for data in dataset:
            self.log_update(data)
