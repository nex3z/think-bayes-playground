from common.util import mean, mean_var


def cov(xs, ys, mux=None, muy=None):
    if mux is None:
        mux = mean(xs)
    if muy is None:
        muy = mean(ys)

    total = 0.0
    for x, y in zip(xs, ys):
        total += (x-mux) * (y-muy)

    return total / len(xs)


def least_squares(xs, ys):
    xbar, varx = mean_var(xs)
    ybar, vary = mean_var(ys)

    slope = cov(xs, ys, xbar, ybar) / varx
    inter = ybar - slope * xbar

    return inter, slope
