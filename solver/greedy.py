import numpy
import random
from world.route import Route


__author__ = 'Ondřej Lanč'


def greedy(world, start=None):
    count=world.city_count
    unvisited=world.cities[:]
    route=Route()
    start=start or unvisited[0]
    actual_city=start
    unvisited.remove(actual_city)
    route.append(actual_city)
    while unvisited:
        next = min([(finish, path.distance) for (finish, path) in actual_city.paths.items() if finish in unvisited], key=lambda x: x[1])
        actual_city=next[0]
        unvisited.remove(actual_city)
        route.append(actual_city)
    route.append(start)
    return route


def greedy_rand(world):
    return greedy(world, random.choice(world.cities))


def greedy_all(world):
    return min([greedy(world, city) for city in world.cities], key=lambda x:x.length())
