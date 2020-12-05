import re
from collections import Counter

xs = open("input", "r").readlines()
tower_pattern = re.compile("(\w+) \((\d+)\)")

# Build up tower list
answer1list = []
tower_dict = {}
parents_dict = {}
for x in xs:
    x = x.rstrip("\n")
    (tower, tower_weight) = tower_pattern.match(x).groups()
    if (" -> " in x):
        (t, ts) = x.split(" -> ")
        subtowers = ts.split(', ')

        for st in subtowers:
            parents_dict[st] = (tower, tower_weight)

        answer1list += [(tower, tower_weight)]

    tower_dict[tower] = tower_weight

# Determine bottom program
bottom_tower = ""
bottom_tower_weight = ""
for (tower, tower_weight) in answer1list:
    if tower not in parents_dict.keys():
        bottom_tower = tower
        bottom_tower_weight = tower_weight
        print "Answer part 1:", tower
        break;

# ANSWER PART 2

# loop recursively over all subtrees
def constructTowerTree(parent):
    subtowers = [st for st, (p, pw) in parents_dict.items() if p == parent]
    tt = {}
    tt = {
        "tower": parent,
        "weight": int(tower_dict[parent]),
        "sumWeight": 0,
        "subtowers": [constructTowerTree(st) for st in subtowers]
    }
    return tt


tower_tree = constructTowerTree(bottom_tower)

def calculateSumWeight(tree):
    if tree["subtowers"] == []:
        return tree["weight"]

    tree["sumWeight"] = tree["weight"] + sum([calculateSumWeight(st) for st in tree["subtowers"]])
    return tree["sumWeight"]

calculateSumWeight(tower_tree)

def determineDiffWeight(tree):
    if tree["subtowers"] == []:
        return;

    sumWeights = [st["sumWeight"] for st in tree["subtowers"]]
    weightCounts = Counter(sumWeights)

    os = weightCounts.keys()
    unbalancedWeight = os[0] if weightCounts[os[0]] < weightCounts[os[1]] else os[1]
    unbalancedSt = [st for st in tree["subtowers"] if st["sumWeight"] == unbalancedWeight][0]

    if 0 in weightCounts.keys():
        return tree["weight"];
    else:
        uw = determineDiffWeight(unbalancedSt)
        if (uw):
            print "Answer part 2:", uw - (os[0] - os[1])

        return;

determineDiffWeight(tower_tree)
