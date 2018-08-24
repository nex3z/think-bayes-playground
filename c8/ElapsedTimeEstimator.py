from c8.Elapsed import Elapsed


class ElapsedTimeEstimator(object):
    def __init__(self, wtc, lam=2.0/60, num_passengers=15):
        self.prior_x = Elapsed(wtc.pmf_x)
        self.post_x = self.prior_x.copy()
        self.post_x.update((lam, num_passengers))
        self.pmf_y = predict_wait_time(wtc.pmf_zb, self.post_x)

    def plot_cdf(self):
        cdf_prior_x = self.prior_x.make_cdf('prior x')
        cdf_post_x = self.post_x.make_cdf('posterior x')
        cdf_y = self.pmf_y.make_cdf('y')
        cdf_prior_x.plot_with([cdf_post_x, cdf_y])


def predict_wait_time(pmf_zb, pmf_x):
    pmf_y = pmf_zb - pmf_x
    remove_negatives(pmf_y)
    return pmf_y


def remove_negatives(pmf):
    pmf.d = pmf.d.loc[pmf.d.value >= 0, ]
    pmf.normalize()
