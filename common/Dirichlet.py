import numpy as np
from common.Beta import Beta


class Dirichlet(object):
    def __init__(self, n):
        self.n = n
        self.params = np.ones(n, dtype=np.int)

    def marginal_beta(self, i):
        alpha0 = self.params.sum()
        alhpa = self.params[i]
        return Beta(alhpa, alpha0 - alhpa)

    def update(self, data):
        m = len(data)
        self.params[:m] += data
