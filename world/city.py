import numpy
from world.path import Path

class City:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        self.paths={}

    def calc_paths(self, cities, func=None):
        self.paths={city: Path(self, city, func) for city in cities}
