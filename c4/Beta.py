class Beta(object):
    def __init__(self, alpha=1, beta=1, name=''):
        self.alpha = alpha
        self.beta = beta
        self.name = name

    def update(self, data):
        heads, tails = data
        self.alpha += heads
        self.beta += tails

    def mean(self):
        return float(self.alpha) / (self.alpha + self.beta)
