import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

from c13.Cache import Cache
from c13.util import rdt_generator, volume, diameter

INTERVAL = 245/365.0


class Calculator(object):
    def __init__(self):
        self.cache = Cache()

    def make_sequences(self, n, rho, cdf):
        sequences = []
        for i in range(n):
            rdt_seq = rdt_generator(cdf, rho)
            seq = self.make_sequence(rdt_seq)
            sequences.append(seq)
            if i % 100 == 0:
                print("{}/{}".format(i + 1, n))
        return sequences

    def make_sequence(self, rdt_seq, v0=0.01, interval=INTERVAL, vmax=volume(20)):
        seq = (v0, )
        age = 0
        for rdt in rdt_seq:
            age += interval
            final, seq = self.extent_sequence(age, seq, rdt, interval)
            if final > vmax:
                break
        return seq

    def extent_sequence(self, age, seq, rdt, interval):
        initial = seq[-1]
        doublings = rdt * interval
        final = initial * 2 ** doublings
        new_seq = seq + (final, )
        self.cache.add(age, new_seq, rdt)
        return final, new_seq


def plot_sequences(sequences):
    fig, ax = plt.subplots()
    plt.ylim((0.2, 20))
    plt.yscale('log')
    for seq in sequences:
        n = len(seq)
        age = n * INTERVAL
        ts = np.linspace(0, age, n)
        plot_sequence(ts, seq)
    ax.get_yaxis().set_major_formatter(ScalarFormatter())
    ax.set_yticks([0.2, 0.5, 1, 2, 5, 10, 20])
    plt.show()


def plot_sequence(ts, seq):
    xs = [diameter(v) for v in seq]
    plt.plot(ts, xs)
