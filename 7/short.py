import networkx as x

g = x.DiGraph()

with open("7/input.txt") as f:

    for l in f.readlines():
        o, i = l.rstrip().split(" contain ")
        b = i.split(", ")
        o = o.rsplit(" ", 1)[0]

        for c in b:
            if c[0] == "n":
                continue
            n, *i, _ = c.split()

            g.add_edge(o, " ".join(i), n=int(n))

# Part 1
s = "shiny gold"

print(len(x.algorithms.dag.ancestors(g, s)))


def t(b): return sum(g[b][c]["n"] * (1 + t(c)) for c in g.successors(b))


print(t(s))
