from functools import reduce
from operator import mul

with open("3/input.txt") as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]
width = len(lines[0])


def compute(right, down):
    trees = 0

    if down > 1:
        right = 0.5

    for i, line in enumerate(lines):
        if down == 1 or not i % 2:
            char = line[int(right * i) % width]
            if char == "#":
                trees += 1

    return trees


steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(reduce(mul, (compute(*x) for x in steps)))
