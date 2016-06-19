import numpy


class Path:
    def __init__(self, start, finish, func=None, pher=0):
        self.distance=self.calc_distance(start, finish, func)
        self.pher=pher
        self.start = start
        self.finish = finish

    def calc_distance(self, start, finish, func=None):
        func = func or self._euclidean_distance
        return func(start, finish)

    def _euclidean_distance(self, start, finish):
        return numpy.linalg.norm(numpy.subtract((finish.x, finish.y), (start.x, start.y)))

    def evaporate(self, func):
        self.pher=func(self.pher)

    def add_ph(self, pher):
        self.pher = self.pher + pher