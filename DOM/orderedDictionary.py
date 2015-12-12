from collections import OrderedDict


class OrderedDictionary(OrderedDict):

    def last(self):
        return self[self.lastKey()]

    def lastKey(self):
        return next(reversed(self))
