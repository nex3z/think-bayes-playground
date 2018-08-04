import c8.c8_util as c8


class WaitTimeCalculator(object):
    def __init__(self, pmf_z):
        self.pmf_z = pmf_z
        self.pmf_zb = c8.bias_pmf(pmf_z)
        self.pmf_y = c8.pmf_of_wait_time(self.pmf_zb)
        self.pmf_x = self.pmf_y