from common.Pmf import Pmf
import common.util as util
from common.EstimatedPdf import EstimatedPdf


OBSERVED_GAP_TIMES = [
    428.0, 705.0, 407.0, 465.0, 433.0, 425.0, 204.0, 506.0, 143.0, 351.0,
    450.0, 598.0, 464.0, 749.0, 341.0, 586.0, 754.0, 256.0, 378.0, 435.0,
    176.0, 405.0, 360.0, 519.0, 648.0, 374.0, 483.0, 537.0, 578.0, 534.0,
    577.0, 619.0, 538.0, 331.0, 186.0, 629.0, 193.0, 360.0, 660.0, 484.0,
    512.0, 315.0, 457.0, 404.0, 740.0, 388.0, 357.0, 485.0, 567.0, 160.0,
    428.0, 387.0, 901.0, 187.0, 622.0, 616.0, 585.0, 474.0, 442.0, 499.0,
    437.0, 620.0, 351.0, 286.0, 373.0, 232.0, 393.0, 745.0, 636.0, 758.0,
]


def get_sample_pmf_z(gap_times=OBSERVED_GAP_TIMES):
    xs = make_range(low=10)
    pdf_z = EstimatedPdf(gap_times)
    pmf_z = pdf_z.make_pmf(xs, name="z")
    return pmf_z


def bias_pmf(pmf, name='', invert=False):
    new_pmf = pmf.copy(name=name)
    for x, p in pmf.iter_items():
        if invert:
            new_pmf.mult(x, 1.0 / x)
        else:
            new_pmf.mult(x, x)
    new_pmf.normalize()
    return new_pmf


def unbias_pmf(pmf, name=''):
    return bias_pmf(pmf, name, invert=True)


def pmf_of_wait_time(pmf_zb):
    meta_pmf = {}
    for gap, prob in pmf_zb.iter_items():
        uniform = make_uniform_pmf(0, gap)
        meta_pmf[uniform] = prob
    pmf_y = util.make_mixture(meta_pmf)
    return pmf_y


def make_uniform_pmf(low, high):
    pmf = Pmf()
    for x in make_range(low, high):
        pmf.set(x, 1)
    pmf.normalize()
    return pmf


def make_range(low=10, high=1200, skip=30):
    return range(low, high + skip, skip)
