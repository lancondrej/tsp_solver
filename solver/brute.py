import itertools
from world.route import Route

def brute(world):
    permutations=itertools.permutations(world.cities)
    min_route_length=99999999999999999
    for perm in permutations:
        route = Route()
        route.route=list(perm)
        route.append(route[0])
        route_length=route.length()
        if min_route_length>route_length:
            min_route_length=route_length
            min_route=route
    return min_route
