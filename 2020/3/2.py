import numpy

def num_of_trees(down, right):
  i = right
  j = down
  maxIndex = len(input[0])

  trees = 0
  while j <= len(input) - 1:
    if input[j][i % maxIndex] == '#':
      trees += 1

    i += right
    j += down
  
  return trees


input = open("input", "r").read().split('\n')

SLOPE_SET=[(1,1),(1,3),(1,5),(1,7),(2,1)]
trees = [num_of_trees(slope[0], slope[1]) for slope in SLOPE_SET]

print('NUMBER OF TREES: ' + str(numpy.prod(trees)))