with open("12/input.txt") as f:
    east = 0
    north = 0
    direction = 90
    for line in f.readlines():
        op = line[0]
        arg = int(line[1:])

        if op == "F":
            op = {0: "N",
                  90: "E",
                  180: "S",
                  270: "W"}[direction]

        if op == "N":
            north += arg
        if op == "S":
            north -= arg
        if op == "E":
            east += arg
        if op == "W":
            east -= arg
        if op == "L":
            direction = (direction - arg) % 360
        if op == "R":
            direction = (direction + arg) % 360

    print(abs(east) + abs(north))

# Part 2


def rot90(w_north, w_east):
    return -w_east, w_north


with open("12/input.txt") as f:
    east = 0
    north = 0
    w_east = 10
    w_north = 1
    for line in f.readlines():
        op = line[0]
        arg = int(line[1:])

        print(op, arg)

        if op == "F":
            north += w_north * arg
            east += w_east * arg

        if op == "L":
            arg = 360 - arg
            op = "R"

        if op == "N":
            w_north += arg
        if op == "S":
            w_north -= arg
        if op == "E":
            w_east += arg
        if op == "W":
            w_east -= arg
        if op == "L":
            direction = (direction - arg) % 360
        if op == "R":
            for _ in range(arg // 90):
                w_north, w_east = rot90(w_north, w_east)

        print(east, north, w_east, w_north)

    print(abs(east) + abs(north))
