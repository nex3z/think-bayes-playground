from common.Pmf import Pmf


class Die(Pmf):
    def __init__(self, sides):
        super().__init__()
        for x in range(1, sides + 1):
            self.set(x, 1)
        self.normalize()
