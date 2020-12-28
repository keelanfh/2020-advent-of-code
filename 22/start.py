from collections import deque

with open("22/input.txt") as f:
    lines = f.read()

lines = lines.split("\n")

cards = {1: deque(), 2: deque()}

for line in lines:
    if line == "":
        continue
    elif line == "Player 1:":
        player = 1
        continue
    elif line == "Player 2:":
        player = 2
        continue
    else:
        cards[player].append(int(line))

while len(cards[1]) > 0 and len(cards[2]) > 0:
    p1, p2 = cards[1].popleft(), cards[2].popleft()
    if p1 > p2:
        cards[1].append(p1)
        cards[1].append(p2)
    if p2 > p1:
        cards[2].append(p2)
        cards[2].append(p1)

winner = cards[1] or cards[2]

total = 0

for x in zip(winner, range(len(winner), 0, -1)):
    total += x[0] * x[1]

print(total)
