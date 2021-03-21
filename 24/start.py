import re
from collections import Counter

direction_to_vector = {"e": (1, 0), "w": (-1, 0),
                       "ne": (0, 1), "sw": (0, -1),
                       "nw": (-1, 1), "se": (1, -1)}

black = True
white = False


def black_neighbours(matrix, i, j):
    neighbours = []
    for v, h in direction_to_vector.values():
        if 0 <= (i2 := i + v) < height:
            if 0 <= (j2 := j + h) < width:
                neighbours.append(matrix[i2][j2])
            else:
                continue

    return neighbours.count(black)


def empty_floor():
    return [[white for _ in range(width)] for _ in range(height)]


def run(matrix):
    new_matrix = empty_floor()
    for i in range(height):
        for j in range(width):
            char = matrix[i][j]
            count = black_neighbours(matrix, i, j)
            if char == black and (count == 0 or count > 2):
                new_matrix[i][j] = white
            elif char == white and count == 2:
                new_matrix[i][j] = black
            else:
                new_matrix[i][j] = char

    return new_matrix


with open("24/input.txt") as f:
    flipped_tiles = []
    for line in f.readlines():
        e = ne = 0
        for x in re.findall("(e|w|se|sw|ne|nw)", line):
            e_diff, ne_diff = direction_to_vector[x]
            e += e_diff
            ne += ne_diff

        flipped_tiles.append((e, ne))

    flipped_tiles = [k
                     for k, v in Counter(flipped_tiles).items()
                     if v % 2]

    print(len(flipped_tiles))

    x_dim, y_dim = [max(abs(min(x)), abs(max(x))) for x in zip(*flipped_tiles)]

    iterations = 100

    width = (iterations + x_dim) * 2
    height = (iterations + y_dim) * 2

    floor = empty_floor()

    for x, y in flipped_tiles:
        floor[iterations + y][iterations + x] = black

    for x in range(iterations):
        floor = run(floor)

    print(sum(row.count(black) for row in floor))
