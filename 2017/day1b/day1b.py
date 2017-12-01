xs = open("input", "r").readline().rstrip("\n")
l = len(xs)
print sum([int(x) for i, x in enumerate(xs) if xs[i]==xs[(i+l/2)%l]])
