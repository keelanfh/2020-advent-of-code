with open("10/input.txt") as f:
    nums = [int(x) for x in f.readlines()]

nums.sort()
nums_rev = nums.copy()
nums_rev.reverse()

nums.insert(0, 0)

# Part 1

jolts = 0
diffs = [0] * 4

while nums_rev:
    adapter = nums_rev.pop()
    diffs[adapter - jolts] += 1
    jolts = adapter

print(diffs[1] * (diffs[3] + 1))

# Part 2

paths_to = {k: 0 for k in nums}

paths_to[0] = 1

for num in nums:
    mult = paths_to[num]

    for diff in (1, 2, 3):
        try:
            paths_to[num + diff] += mult
        except KeyError:
            pass

print(paths_to[max(nums)])
