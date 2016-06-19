__author__ = 'Ondřej Lanč'
from solver.ACO.ant import Ant

class Colony:
    def __init__(self, world, ant_count, waves=100, rho=0.8, alpha=1, beta=2, gamma=0.1):
        self.world = world
        self.ants= self.generate_ants(10, alpha, beta, gamma)
        self.rho = rho
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.waves=waves

    def generate_ants(self, count, alpha, beta, gamma, pheromone=1):
        return [Ant(self.world, alpha, beta, gamma, pheromone) for i in range(count)]

    def reset_ants(self):
        for ant in self.ants:
            ant.__init__(self. world, self.alpha, self.beta, self.gamma)

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

        for wave in range(self.waves):
            print(i)
            i+=1
            routes=[ant.find_route() for ant in self.ants]
            routes=[(route, route.length()) for route in routes]
            act_best=min(routes, key=lambda x: x[1])
            if act_best[1] < best:
                best_route = act_best[0]
                best = act_best[1]
            self.evaporate_paths()
            for ant in self.ants:
                ant.set_pheromone()
            self.reset_ants()
        return best_route, (ina ,r)

