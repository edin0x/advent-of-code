import math
input = open("input", "r").read().split('\n')

def calcFuel(m):
  additionalFuel = int(int(m)/3)-2
  if additionalFuel <= 0:
    return 0
  
  return additionalFuel + calcFuel(additionalFuel)

masses = [int(x) for x in input]
fuels = [calcFuel(m) for m in masses]

answer = sum(fuels)
print ('ANSWER: ' + str(answer))