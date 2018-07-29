from common.Pdf import Pdf
import scipy.stats


class GaussianPdf(Pdf):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def density(self, x):
        return scipy.stats.norm.pdf(x, self.mu, self.sigma)
