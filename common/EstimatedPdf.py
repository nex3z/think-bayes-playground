import numpy as np
import scipy.stats

from common.Pdf import Pdf


class EstimatedPdf(Pdf):
    def __init__(self, sample):
        self.kde = scipy.stats.gaussian_kde(sample)

    def density(self, x):
        result = self.kde.evaluate(x)
        return result[0] if np.isscalar(x) else result
