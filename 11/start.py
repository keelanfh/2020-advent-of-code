from itertools import chain, count
matrix = []

with open("11/input.txt") as f:
    for i, line in enumerate(f.readlines()):
        matrix.append([])
        matrix[i] = [x for x in line.strip()]

height = len(matrix)
width = len(matrix[0])


def get_neighbours(i, j, mode=1):
    neighbours = []
    for v, h in [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                 (0, 1), (1, -1), (1, 0), (1, 1)]:
        for mult in count(1):
            if 0 <= (i2 := i + v * mult) < height:
                if 0 <= (j2 := j + h * mult) < width:
                    if mode == 1 or matrix[i2][j2] != ".":
                        neighbours.append(matrix[i2][j2])
                        break
                    else:
                        continue
                else:
                    break
            else:
                break

    return neighbours.count("#")


def run(matrix, mode=1):
    new_matrix = [[0 for col in range(width)] for col in range(height)]
    for i in range(height):
        for j in range(width):
            char = matrix[i][j]
            count = get_neighbours(i, j, mode)
            if char == "L" and count == 0:
                new_matrix[i][j] = "#"
            elif char == "#" and (count - mode) >= 3:
                new_matrix[i][j] = "L"
            else:
                new_matrix[i][j] = char

    if matrix == new_matrix:
        raise RuntimeError

    return new_matrix

# Part 1


while True:
    try:
        matrix = run(matrix)
    except RuntimeError:
        print(sum(row.count("#") for row in matrix))
        break

# Part 2
# Opening the file again so we have a fresh matrix

matrix = []
with open("11/input.txt") as f:
    for i, line in enumerate(f.readlines()):
        matrix.append([])
        matrix[i] = [x for x in line.strip()]

height = len(matrix)
width = len(matrix[0])

while True:
    try:
        matrix = run(matrix, mode=2)
    except RuntimeError:
        print(sum(row.count("#") for row in matrix))
        break
