__author__ = 'Ondřej Lanč'

import matplotlib.pyplot as plt
from world.world import World
from solver.greedy import greedy_all
from solver.brute import brute
from solver.held_karp import hk
import timeit
from solver.ACO.colony import Colony


count_of_cities = 12
upper_bound = 1000
city_seed = 8
world=World()
world.random_world(count_of_cities, upper_bound, upper_bound, city_seed)

print("greedy")
start_time = timeit.default_timer()
route=greedy_all(world)
distance=route.length()
print(distance)
print(timeit.default_timer() - start_time)

# print("brute")
# start_time = timeit.default_timer()
# route=brute(world)
# distance=route.length()
# print(distance)
# print(timeit.default_timer() - start_time)

print("HK")
start_time = timeit.default_timer()
route=hk(world)
distance=route.length()
print(distance)
print(timeit.default_timer() - start_time)

# print("ACO")
# start_time = timeit.default_timer()
# colony = Colony(world, 50, 100, 0.5, 2, 1, 0.2, 100)
# route, routes=colony.solve()
# distance=route.length()
# print(distance)
# print(timeit.default_timer() - start_time)

