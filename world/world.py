from world.city import City
import random
import matplotlib.pyplot as plt


class World:
    def __init__(self):
        self.cities = []
        self._paths = None

    @property
    def city_count(self):
        return len(self.cities)

    def random_world(self, count, x_upper_bound, y_upper_bound, seed):
        random.seed(seed)
        self.cities=[City(x_upper_bound * random.random(), y_upper_bound * random.random()) for i in range(count)]
        self.calc_paths()

    def calc_paths(self, distance=None):
        for city in self.cities:
            city.calc_paths(self.cities, distance)

    def plot(self, route=None, start=None):
        cts = [(city.x, city.y) for city in self.cities]
        fig = plt.figure()
        plt.axis('equal')
        if route:
            plt.plot(*zip(*[(city.x, city.y) for city in route]))
        plt.plot(*zip(*cts), 'ro')
        if start:
            plt.plot(*zip((start.x, start.y)), 'go')
        return fig

    @property
    def paths(self):
        if not self._paths:
            self._paths = [path for city in self.cities for (next, path) in city.paths.items()]
        return self._paths

    def reset_pher(self):
        for path in self.paths:
            path.pher=0
