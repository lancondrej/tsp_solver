__author__ = 'Ondřej Lanč'
from solver.ACO.ant import Ant

class Colony:
    def __init__(self, world, ant_count, rho=0.5, alpha=2, beta=1, gamma=0.1):
        self.world = world
        self.ants= self.generate_ants(ant_count, alpha, beta, gamma)
        self.rho = rho
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    def generate_ants(self, count, alpha, beta, gamma, pheromone=1):
        return [Ant(self.world, alpha, beta, gamma, pheromone) for i in range(count)]

    def evaporate_paths(self):
        for path in self.world.paths:
            path.evaporate(self.evaporate)

    def evaporate(self, pher):
        return pher*self.rho

    def solve(self):
        best=99999999999999999999999999
        best_route=None
        i=0
        ina=[]
        r=[]
        for ant in self.ants:
            route = ant.find_route()
            act_len=route.length()
            ina.append(i)
            r.append(act_len)
            print(i, ". ", act_len)
            i += 1
            if act_len < best:
                best_route = route
                best = act_len
            self.evaporate_paths()

        return best_route, (ina ,r)

