input = open("input", "r").read().split('\n')

DOWN=1
RIGHT=3

i = RIGHT
j = DOWN
maxIndex = len(input[0])

trees = 0
while j <= len(input) - 1:
  if input[j][i % maxIndex] == '#':
    trees += 1

  i += RIGHT
  j += DOWN

print('NUMBER OF TREES: ' + str(trees))