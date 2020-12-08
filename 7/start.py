import networkx

g = networkx.DiGraph()

with open("7/input.txt") as f:

    for l in f.readlines():
        outer_bag, inner_bags = l.rstrip().split(" contain ")
        inner_bags = inner_bags.split(", ")
        *o_colour, _ = outer_bag.split()

        for inner_bag in inner_bags:
            if inner_bag == "no other bags.":
                continue
            i_number, *i_colour, _ = inner_bag.split()

            g.add_edge(" ".join(o_colour),
                       " ".join(i_colour), number=int(i_number))

# Part 1

print(len(networkx.algorithms.dag.ancestors(g, "shiny gold")))

# Part 2


def total_bags_inside(bag: str) -> int:
    if not (successors := g.successors(bag)):
        return 0
    return sum(g[bag][i_bag]["number"] * (1 + total_bags_inside(i_bag))
               for i_bag in successors)


print(total_bags_inside("shiny gold"))
