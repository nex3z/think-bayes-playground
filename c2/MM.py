from common.Suite import Suite


class MM(Suite):
    mix_94 = {'brown': 30, 'yellow': 20, 'red': 20, 'green': 10, 'orange': 10, 'tan': 10, 'blue': 0}
    mix_96 = {'blue': 24, 'green': 20, 'orange': 16, 'yellow': 14, 'red': 13, 'brown': 13, 'tan': 0}
    hypo_a = {'Bag 1': mix_94, 'Bag 2': mix_96}
    hypo_b = {'Bag 1': mix_96, 'Bag 2': mix_94}
    hypotheses=dict(A=hypo_a, B=hypo_b)

    def likelihood(self, data, hypo):
        bag, color = data
        mix = self.hypotheses[hypo][bag]
        like = mix[color]
        return like
