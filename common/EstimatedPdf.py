from common.Pdf import Pdf
import scipy.stats


class EstimatedPdf(Pdf):
    def __init__(self, sample):
        self.kde = scipy.stats.gaussian_kde(sample)

    def density(self, x):
        return self.kde.evaluate(x)
