from c13.util import *
from common.Joint import Joint


class Cache(object):
    def __init__(self):
        self.joint = Joint()

    def add(self, age, seq, rdt):
        final = seq[-1]
        cm = diameter(final)
        bucket = cm_to_bucket(cm)
        self.joint.incr((age, bucket))

    def conditional_cdf(self, bucket, name=""):
        pmf = self.joint.conditional(0, 1, bucket)
        cdf = pmf.make_cdf(name=name)
        return cdf

    def prob_older(self, cm, age):
        bucket = cm_to_bucket(cm)
        cdf = self.conditional_cdf(bucket)
        p = cdf.prob(age)
        return 1 - p
