__author__ = 'Ondřej Lanč'
from solver.ACO.ant import Ant
import random

class Colony:
    def __init__(self, world, ant_count, waves, rho=0.8, alpha=1, beta=2, gamma=0.1, elite=1, start=None):
        self.world = world
        self.rho = rho
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.waves=waves
        self.elite=elite
        self.start=start
        self.ants= self.generate_ants(ant_count, alpha, beta, gamma)


    def generate_ants(self, count, alpha, beta, gamma):
        return [Ant(self.world, alpha, beta, gamma, self.start) for i in range(count)]

    def reset_ants(self):
        for ant in self.ants:
            ant.__init__(self. world, self.alpha, self.beta, self.gamma, self.start)

    def evaporate_paths(self):
        for path in self.world.paths:
            path.evaporate(self.rho)

    def solve(self):
        best=99999999999999999999999999
        best_route=None
        i=0
        ina=[]
        r=[]

        for wave in range(self.waves):
            routes=[(ant, ant.find_route()) for ant in self.ants]
            routes=[(route[0], route[1], route[1].length()) for route in routes]
            act_best=min(routes, key=lambda x: x[2])
            # print(i, ". ", act_best[1])
            ina.append(i)
            r.append(act_best[2])
            i+=1
            act_best[0].pheromone *= self.elite
            if act_best[2] < best:
                best_route = act_best[1]
                best = act_best[2]
            self.evaporate_paths()
            for ant in self.ants:
                ant.set_pheromone()
            self.reset_ants()
        return best_route, (ina ,r)

