import re
m = max(i := [int(re.sub("B|R", "1", re.sub("F|L", "0", l)), 2)
              for l in open("5/input.txt").readlines()])
print(m, max(set(range(m)).difference(i)))
