from c8.c8_util import bias_pmf, pmf_of_wait_time


class WaitTimeCalculator(object):
    def __init__(self, pmf_z):
        self.pmf_z = pmf_z
        self.pmf_zb = bias_pmf(pmf_z)
        self.pmf_y = pmf_of_wait_time(self.pmf_zb)
        self.pmf_x = self.pmf_y

    def plot_cdf(self):
        cdf_z = self.pmf_z.make_cdf(name='z')
        cdf_zb = self.pmf_zb.make_cdf(name='zb')
        cdf_y = self.pmf_y.make_cdf(name='y')
        cdf_z.plot_with([cdf_zb, cdf_y])
