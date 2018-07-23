from common.Suite import Suite


class MM(Suite):
    mix_94 = dict(brown=30, yellow=20, red=20, green=10, orange=10, tan=10, blue=0)
    mix_96 = dict(blue=24, green=20, orange=16, yellow=14, red=13, brown=13, tan=0)
    hypo_a = dict(bag1=mix_94, bag2=mix_96)
    hypo_b = dict(bag1=mix_96, bag2=mix_94)
    hypotheses=dict(A=hypo_a, B=hypo_b)

    def likelihood(self, data, hypo):
        bag, color = data
        mix = self.hypotheses[hypo][bag]
        like = mix[color]
        return like
