import pandas as pd


class Interpolator(object):
    def __init__(self, xs, ys):
        self.d = pd.DataFrame({'x': xs, 'y': ys})

    def lookup(self, x):
        return self.bisect(x, self.d.x, self.d.y)

    def reverse(self, y):
        return self.bisect(y, self.d.y, self.d.x)

    @staticmethod
    def bisect(x, xs, ys):
        if x <= xs.iat[0]:
            return ys.iat[0]
        if x >= xs.iat[-1]:
            return ys.iat[-1]
        pos = xs.searchsorted(x)[0]
        fraction = 1.0 * (x - xs[pos - 1]) / (xs[pos] - xs[pos - 1])
        y = ys[pos - 1] + 1.0 * fraction * (ys[pos] - ys[pos - 1])
        return y
