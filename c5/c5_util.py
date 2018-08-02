from common.Pmf import Pmf


def random_sum(dists):
    return sum(dist.random() for dist in dists)


def sample_sum(dists, n, name=''):
    values = [random_sum(dists) for _ in range(n)]
    pmf = Pmf(name=name)
    for value in values:
        pmf.incr(value)
    pmf.normalize()
    return pmf


def random_max(dists):
    return max(dist.random() for dist in dists)


def sample_max(dists, n, name=''):
    values = [random_max(dists) for _ in range(n)]
    # print(values)
    pmf = Pmf(name=name)
    for value in values:
        pmf.incr(value)
    pmf.normalize()
    return pmf


def pmf_max(pmf_1, pmf_2, name=''):
    name = name if name else pmf_1.name
    pmf = Pmf(name=name)
    for v1, p1 in pmf_1.iter_items():
        for v2, p2 in pmf_2.iter_items():
            pmf.incr(max(v1, v2), p1 * p2)
    return pmf
