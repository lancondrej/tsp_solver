__author__ = 'Ondřej Lanč'
from solver.ACO.ant import Ant

class Colony:
    def __init__(self, world, ant_count, delta=0.7):
        self.world = world
        self.generate_colony(ant_count)
        self.delta = delta

    def generate_colony(self, count):
        self.ants=[Ant(self.world) for i in range(count)]

    def evaporate_paths(self):
        for path in self.world.paths:
            path.evaporate(self.evaporate)

    def evaporate(self, pher):
        return pher*self.delta

    def solve(self):
        best=99999999999999999999999999
        best_route=None
        for ant in self.ants:
            route = ant.find_route()
            act_len=route.length()
            if act_len < best:
                best_route = route
                best = act_len
            self.evaporate_paths()
        return best_route

