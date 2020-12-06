from functools import reduce
g = open("6/input.txt").read().split("\n\n")
print(sum(len(set(x for x in h if x != "\n")) for h in g),
      sum(len(reduce(set.intersection, (set(x) for x in h.split())))
          for h in g))
