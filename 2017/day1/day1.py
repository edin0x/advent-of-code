xs = open("input", "r").readline().rstrip("\n")
l = len(xs)
print "Answer part one:", sum([int(x) for i, x in enumerate(xs) if xs[i]==xs[(i+1)%l]])
print "Answer part two:", sum([int(x) for i, x in enumerate(xs) if xs[i]==xs[(i+l/2)%l]])
