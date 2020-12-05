import re

xs = open("input", "r").readlines()
tower_pattern = re.compile("(\w+) \((\d+)\)")

# Build up tower list
towerlist = []
towerdict = {}
for x in xs:
    x = x.rstrip("\n")
    if (" -> " in x):
        (t, ts) = x.split(" -> ")
        (tower, tower_weight) = tower_pattern.match(t).groups()
        subtowers = ts.split(', ')

        for st in subtowers:
            towerdict[st] = tower

        towerlist += [tower]

        #towerlist += [(tower, tower_weight, subtowers)]
    #else:
    #    (tower, tower_weight) = tower_pattern.match(x).groups()
    #    towerlist += [(tower, tower_weight, [])]

# Determine bottom program
for t in towerlist:
    if t not in towerdict.keys():
        print "Answer part 1:", t
