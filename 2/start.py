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

    import re
    valid = 0

    for line in f.readlines():
        rg, letter, password = line.split()
        letter = letter[0]
        fr, to = rg.split("-")
        print(password, letter)
        print(re.finditer(letter, password))

        break

        if x := password.index(letter) == int(fr) - 1 or x == int(to) - 1:
            if password.count(letter) == 1:
                valid += 1

                # print(valid)
