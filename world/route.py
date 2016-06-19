class Route:
    def __init__(self):
        self.route = []

    def __getitem__(self, key):
        return self.route[key]

    def append(self, item):
        self.route.append(item)

    def length(self, route=None):
        route=route or self.route
        subroute = route[:]
        city = subroute.pop(0)
        if subroute:
            dist=city.paths[subroute[0]].distance+self.length(subroute)
            return dist
        return 0

    @property
    def paths(self):
        a= [self.route[index-1].paths[city] for index, city in list(enumerate(self.route))[1:]]
        return a

    @property
    def rpaths(self):
        rr=self.route[:]
        rr.reverse()
        a= [self.route[index-1].paths[city] for index, city in list(enumerate(rr))[1:]]
        return a