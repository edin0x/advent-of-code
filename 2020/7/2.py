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

def findNumOfBags(color):
  if bagDictionary[color] == [] or (color not in bagDictionary.keys()):
    return 1
  
  return 1 + sum([int(sb[0])*findNumOfBags(sb[1]) for sb in bagDictionary[color]])
  
answer = findNumOfBags("shiny gold")

print('ANSWER: ' + str(answer-1))