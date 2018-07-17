from common.Suite import Suite


class MontySuite(Suite):
    def likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1
