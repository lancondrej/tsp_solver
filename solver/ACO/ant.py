import random
from world.route import Route
import itertools
import bisect

class Ant:
    def __init__(self, world, alpha=0.4, beta=2, gamma=0.1, start=None):
        self.alpha = alpha
        self.beta = beta
        self.gamma =gamma
        self.position = start or random.choice(world.cities)
        self.route = Route()
        self.unvisited = world.cities[:]
        self.pheromone = 100
        self.world = world

    def move(self):
        self.unvisited.remove(self.position)
        self.route.append(self.position)
        self.position=self.choose_move()

    def find_route(self):
        while self.unvisited:
            self.move()
        self.route.append(self.route[0])
        return self.route

    def set_pheromone(self):
        ph=self.pheromone / self.route.length()
        for path in self.route.paths:
            path.add_ph(ph)
        # for path in self.route.rpaths:
        #     path.add_ph(ph)


    def choose_move(self):
        if len(self.unvisited) == 0:
            return None
        if len(self.unvisited) == 1:
            return self.unvisited[0]

        available, weights = zip(*sorted([(city, ((1.0/path.distance) ** self.alpha) * (1+ path.pher ** self.beta)) for (city, path) in self.position.paths.items() if city in self.unvisited], key=lambda x: x[1]))
        total = sum(weights)
        dist = list(itertools.accumulate(weights))
        dist.pop()
        vyb=available[bisect.bisect(dist, (random.random()**self.gamma) * total)]
        return vyb

