from common.Suite import Suite


class MM(Suite):
    mix94 = dict(brown=30, yellow=20, red=20, green=10, orange=10, tan=10, blue=0)
    mix96 = dict(blue=24, green=20, orange=16, yellow=14, red=13, brown=13, tan=0)
    hypoA = dict(bag1=mix94, bag2=mix96)
    hypoB = dict(bag1=mix96, bag2=mix94)
    hypotheses=dict(A=hypoA, B=hypoB)

    def likelihood(self, data, hypo):
        bag, color = data
        mix = self.hypotheses[hypo][bag]
        like = mix[color]
        return like
