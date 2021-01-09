from itertools import count

with open("13/input.txt") as f:
    start, routes = f.readlines()

start = int(start)
routes = routes.split(",")
routes = [int(x) if x != "x" else None for x in routes]
routes_1 = [int(x) for x in routes if x]

# Part 1


def find_route_1():
    for time in count(start):
        for route in routes_1:
            if not time % route:
                return route * (time - start)


print(find_route_1())

# Part 2

routes_2 = [(index, route) for index, route in enumerate(routes) if route]


def find_route_2():
    time = 0
    step = 1
    index, route = routes_2.pop()
    while True:
        if not (time + index) % route:
            step *= route
            try:
                index, route = routes_2.pop()
            except IndexError:
                return time
        else:
            time += step


print(find_route_2())
