from common.Pmf import Pmf
from common.util import make_poisson_pmf, make_exponential_pmf, make_mixture


def make_goal_pmf(suite):
    meta_pmf = Pmf()
    for lam, prob in suite.iter_items():
        pmf = make_poisson_pmf(lam, 10)
        meta_pmf.set(pmf, prob)
    mix = make_mixture(meta_pmf, name=suite.name)
    return mix


def make_goal_time_pmf(suite):
    pmfs = [make_exponential_pmf(lam, high=2, n=201) for lam, _ in suite.iter_items()]
    probs = [prob for _, prob in suite.iter_items()]
    meta_pmf = Pmf(values=pmfs, probs=probs)
    mix = make_mixture(meta_pmf, name=suite.name)
    return mix
