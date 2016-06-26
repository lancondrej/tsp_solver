__author__ = 'Ondřej Lanč'
from world.route import Route

def hk_sub(start, city_subset, end):
    if city_subset == set():
        return start.paths[end].distance, [end]
    else:
        routes=[]
        for c in city_subset:
            sub=hk_sub(start, city_subset.difference(set([c])), c)
            r = Route()
            r.route = sub[1][:]
            r.append(c)
            routes.append((sub[0]+c.paths[end].distance, r))
        minr=min(routes, key=lambda x: x[0])
        return minr

# Held–Karp solver
def hk(world):
    city_set = set(world.cities)
    start=world.cities[0]
    routes = []
    for c in city_set.difference(set([start])):
        sub = hk_sub(start, city_set.difference(set([start, c])), c)
        r=Route()
        r.route = [start] + sub[1][:]
        r.append(c)
        r.append(start)
        routes.append((sub[0] + c.paths[start].distance, r))
    minr = min(routes, key=lambda x: x[0])
    return minr[1]



