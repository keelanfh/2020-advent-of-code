import re

with open("2/input.txt") as f:

    # Part 1

    valid = 0

    for line in f.readlines():
        rg, letter, password = line.split()
        letter = letter[0]
        fr, to = rg.split("-")
        if int(fr) <= password.count(letter) <= int(to):
            valid += 1

    print(valid)

# Part 2

with open("2/input.txt") as f:

    valid = 0

    for line in f.readlines():
        rg, letter, password = line.split()
        letter = letter[0]
        fr, to = rg.split("-")
        pos = [x.span()[1] for x in re.finditer(letter, password)]

        if (int(fr) in pos) ^ (int(to) in pos):
            valid += 1

    print(valid)
