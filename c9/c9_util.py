import math

from common.Pmf import Pmf


def strafing_speed(alpha, beta, x):
    theta = math.atan2(x - alpha, beta)
    speed = beta / math.cos(theta) ** 2
    return speed


def make_location_pmf(alpha, beta, locations, name=''):
    probs = [1.0 / strafing_speed(alpha, beta, x) for x in locations]
    pmf = Pmf(values=locations, probs=probs, name=name)
    return pmf
