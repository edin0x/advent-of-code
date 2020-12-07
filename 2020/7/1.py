import re
input = open("input", "r").read().split('\n')

bagDictionary = {}
for line in input:
  mainBag, subBagString = re.search(r"(\w+ \w+) bags contain (.*)\.", line).groups()
  if ("no other bags" not in subBagString):
    subBags = [re.match(r"(\d+) (\w+ \w+) bags?", bd).groups() for bd in subBagString.split(', ')]
    bagDictionary[mainBag] = subBags
  else:
    bagDictionary[mainBag] = []

def findColorsContaining(color):
  if bagDictionary[color] == [] or (color not in bagDictionary.keys()):
    return []
  
  parentColors = [k for k,vs in bagDictionary.items() for v in vs if v[1] == color]

  ppc = []
  for pc in parentColors:
    ppc += findColorsContaining(pc)
  
  return parentColors + ppc
  
allColors = findColorsContaining("shiny gold")
answer = len(set(allColors))

print('ANSWER: ' + str(answer))