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
        return [city.paths[next] for city in self.route for next in self.route[1:]]