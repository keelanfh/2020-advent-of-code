with open("1/input.txt") as f:
    nums = f.readlines()

    # Part 1

    ints = [int(x) for x in nums]
    for i in ints:
        for j in ints:
            if i + j == 2020:
                print(i * j)

    # Part 2

    ints = [int(x) for x in nums]
    for i in ints:
        for j in ints:
            for k in ints:
                if sum((i, j, k)) == 2020:
                    print(i * j * k)
