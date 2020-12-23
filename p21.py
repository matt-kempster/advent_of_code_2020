from pathlib import Path
import itertools
from typing import Dict, Tuple, Set, List
from copy import copy


def main():
    all_allergens = set()
    identity_8 = [[int(i == j) for j in range(8)] for i in range(8)]
    eggs = identity_8[0]
    sesame = identity_8[1]
    nuts = identity_8[2]
    wheat = identity_8[3]
    shellfish = identity_8[4]
    peanuts = identity_8[5]
    dairy = identity_8[6]
    soy = identity_8[7]

    mapping: Dict[Tuple[int, ...], Set[str]] = {}
    contents = Path("./inputs/p21.txt").read_text()
    indicators = []
    for line in contents.split("\n"):
        if not line.strip():
            continue
        [ingredients_str, allergens_str] = line.strip(" )").split("(contains")
        ingredients = set(ingredients_str.split())
        allergens = set(allergens_str.strip().split(", "))
        indicator = [0] * 8
        for (name, value) in (
            ("eggs", eggs),
            ("sesame", sesame),
            ("nuts", nuts),
            ("wheat", wheat),
            ("shellfish", shellfish),
            ("peanuts", peanuts),
            ("dairy", dairy),
            ("soy", soy),
        ):
            if name in allergens:
                indicator = list(map(sum, zip(indicator, value)))
        print(list(indicator))
        indicators.append(list(indicator))
        all_allergens |= allergens
        mapping[tuple(indicator)] = ingredients

    ## This just figures out that there are no pairs that are glued together:
    # for (allergen_1, allergen_2) in itertools.combinations(identity_8, 2):
    #     pair = list(map(lambda x: x[0] | x[1], zip(allergen_1, allergen_2)))
    #     never_together = True
    #     for indicator in indicators:
    #         zero_one_or_two = list(map(lambda x: x[0] & x[1], zip(pair, indicator)))
    #         if sum(zero_one_or_two) == 1:
    #             # Good!
    #             break
    #         elif sum(zero_one_or_two) == 2:
    #             never_together = False
    #     else:
    #         if not never_together:
    #             # Bad :(
    #             print(f"Cannot distinguish: {pair}")
    for allergen_indicator in identity_8:
        possible_ingredients: Set[str] = set()
        for indicator in indicators:
            # import pdb; pdb.set_trace()
            if sum(map(lambda x: x[0] & x[1], zip(allergen_indicator, indicator))) == 0:
                continue
            if not possible_ingredients:
                # First one.
                possible_ingredients = copy(mapping[tuple(indicator)])
            else:
                possible_ingredients &= mapping[tuple(indicator)]
        print(f"{allergen_indicator}: {possible_ingredients}")


def main2():
    result = {
        [1, 0, 0, 0, 0, 0, 0, 0]: {"gzvsg", "xblchx", "tr"},
        [0, 1, 0, 0, 0, 0, 0, 0]: {"gzvsg", "jlsqx"},
        [0, 0, 1, 0, 0, 0, 0, 0]: {"gzvsg", "tr"},
        [0, 0, 0, 1, 0, 0, 0, 0]: {"csqc", "gzvsg", "lvv", "pmz"},
        [0, 0, 0, 0, 1, 0, 0, 0]: {"csqc", "gzvsg", "jlsqx", "fnntr"},
        [0, 0, 0, 0, 0, 1, 0, 0]: {"gzvsg", "pmz"},
        [0, 0, 0, 0, 0, 0, 1, 0]: {"xblchx", "lvv"},
        [0, 0, 0, 0, 0, 0, 0, 1]: {"jlsqx", "pmz"},
    }
    # One solution:
    #  xblchx, gzvsg, tr, csqc, fnntr, pmz, lvv, jlsqx
    #  xblchx, jlsqx, tr, csqc, fnntr, gzvsg, lvv, pmz
    # That uses up everything. Therefore they can all possibly be allergens.


def main3():
    contents = Path("./inputs/p21.txt").read_text()
    ingredient_count = 0
    for line in contents.split("\n"):
        if not line.strip():
            continue
        [ingredients_str, allergens_str] = line.strip(" )").split("(contains")
        ingredients = set(ingredients_str.split())
        ingredients -= {"jlsqx", "fnntr", "csqc", "xblchx", "pmz", "gzvsg", "tr", "lvv"}
        ingredient_count += len(ingredients)
    print(ingredient_count)

    # For Part 2, I guess I got lucky in finding that solution above, as it has
    # to be the only solution.
    # So now I need to arrange the allergens alphabetically...
    eggs = identity_8[0]
    sesame = identity_8[1]
    nuts = identity_8[2]
    wheat = identity_8[3]
    shellfish = identity_8[4]
    peanuts = identity_8[5]
    dairy = identity_8[6]
    soy = identity_8[7]


result = {
    [0, 0, 0, 0, 0, 0, 1, 0]: ("dairy", "lvv"),
    [1, 0, 0, 0, 0, 0, 0, 0]: ("eggs", "xblchx"),
    [0, 0, 1, 0, 0, 0, 0, 0]: ("nuts", "tr"),
    [0, 0, 0, 0, 0, 1, 0, 0]: ("peanuts", "gzvsg"),
    [0, 1, 0, 0, 0, 0, 0, 0]: ("sesame", "jlsqx"),
    [0, 0, 0, 0, 1, 0, 0, 0]: ("shellfish", "fnntr"),
    [0, 0, 0, 0, 0, 0, 0, 1]: ("soy", "pmz"),
    [0, 0, 0, 1, 0, 0, 0, 0]: ("wheat", "csqc"),
}
# lvv,xblchx,tr,pmz,gzvsg,fnntr,jlsqx,csqc
# lvv,xblchx,tr,gzvsg,jlsqx,fnntr,pmz,csqc
# Why are there two solutions... I'm not sure.

if __name__ == "__main__":
    # main()
    # main2()
    main3()
