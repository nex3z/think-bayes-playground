class DictWrapper(object):
    def __init__(self, values=None, name=''):
        self.name = name
        self.d = {}

        if values is None:
            return

        for method in [self.__init_sequence, self.__init_map, self.__init_failure]:
            try:
                method(values)
                break
            except AttributeError:
                continue

    def __init_sequence(self, keys):
        for key in keys:
            self.set(key, 1)

    def __init_map(self, mapping):
        for key, value in mapping.items():
            self.set(key, value)

    def __init_failure(self, values):
        raise ValueError('Initialization failed')

    def set(self, key, value):
        self.d[key] = value

    def mult(self, key, factor):
        self.d[key] = self.d.get(key, 0) * factor

    def total(self):
        return sum(self.d.values())
