from itertools import permutations, count, tee

with open("9/input.txt") as f:
    nums = [int(x) for x in f.readlines()]


def all_sums(numbers: list):
    return (set(sum(x) for x in permutations(numbers, r=2) if x[0] != x[1]))


for i, num in enumerate(nums[25:]):
    sums = all_sums(nums[i: i + 25])
    if num not in sums:
        invalid = num

print(invalid)


def nwise(n, iter):
    iters = tee(iter, n)
    for i in range(n):
        for _ in range(i):
            next(iters[i], None)
    return zip(*iters)


def check_all():
    for i in count(2):
        groups = nwise(i, nums)
        for g in groups:
            if sum(g) == invalid:
                print(min(g)+max(g))
                return


check_all()
