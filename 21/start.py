from functools import reduce
import operator

with open("21/input.txt") as f:
    allergens_to_ingredients = dict()
    all_ingredients = []

    for line in f.readlines():
        ingredients, allergens = line.split(" (contains ")
        ingredients = ingredients.split(" ")
        allergens = allergens.split(")")[0].split(", ")
        all_ingredients += ingredients

        for allergen in allergens:
            try:
                allergens_to_ingredients[allergen] &= set(ingredients)
            except KeyError:
                allergens_to_ingredients[allergen] = set(ingredients)

    allergenic_ingredients = reduce(
        set.union, allergens_to_ingredients.values())
    print(len([x for x in all_ingredients if x not in allergenic_ingredients]))

    used_fields = set()
    while any(len(v) > 1 for v in allergens_to_ingredients.values()):
        for k, v in allergens_to_ingredients.items():
            if len(v) == 1:
                used_fields.add(next(iter(v)))
            else:
                allergens_to_ingredients[k] = {f
                                               for f in allergens_to_ingredients[k]
                                               if f not in used_fields}

    print(",".join([x[1]
                    for x in sorted([(allergen, ingredient.pop())
                                     for allergen, ingredient in allergens_to_ingredients.items()])]))
