from c14.Detector import Detector
from common.Pmf import Pmf
from common.Suite import Suite
from common.util import make_mixture


class Emitter(Suite):
    def __init__(self, rs, f=0.1):
        detectors = [Detector(r, f) for r in rs]
        super().__init__(detectors)

    def likelihood(self, data, hypo):
        detector = hypo
        like = detector.suite_likelihood(data)
        return like

    def update(self, data):
        super(Emitter, self).update(data)
        for detector in self.values():
            detector.update(data)

    def dist_of_r(self, name=""):
        values = [detector.r for detector, _ in self.iter_items()]
        pmf = Pmf(values=values, probs=self.probs(), name=name)
        return pmf

    def dist_of_n(self, name=""):
        return make_mixture(self, name=name)
