with open("5/input.txt") as f:
    lines = f.readlines()

    all = []

    for line in lines:
        vert = int(line[:7].replace("F", "0").replace("B", "1"), base=2)
        hor = int(line[7:10].replace("L", "0").replace("R", "1"), base=2)

        all.append((vert, hor))

    ids = [a * 8 + b for a, b in all]
    lowest, highest = min(ids), max(ids)

    print(highest)

    print(set(range(lowest, highest)).difference(ids).pop())
