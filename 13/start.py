from numpy import array
import timeit
from itertools import count
from dis import dis

with open("13/input.txt") as f:
    start, routes = f.readlines()

start = int(start)
routes_x = [int(x) if x != "x" else None for x in routes.split(",")]
routes = [int(x) for x in routes.split(",") if x != "x"]

# Part 1


def find_route():
    for time in count(start):
        for route in routes:
            if not time % route:
                return route * (time - start)


print(find_route())

# Part 2

print(routes_x)

# print(509 - routes.index(509), 509)

routes_li = [route for index, route in enumerate(routes_x) if route]

routes = [(index, route) for index, route in enumerate(routes_x) if route]
routes.sort(key=lambda x: x[1])
routes.reverse()
print(routes)
# routes = array(routes)


def calculate():
    for time in count(max(routes_li) - routes_li.index(max(routes_li)), max(routes_li)):
        for index, route in routes:
            # If it doesn't match
            if (time + index) % route:
                break
            # Otherwise
            else:
                continue
        else:
            print(time)
            break
        print(time)


print(timeit.timeit(calculate, number=5))
