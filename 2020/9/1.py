import re
input = open("input", "r").read().split('\n')
input = [int(i) for i in input]

PREAMBLE = 25

def checkPreamble(i, inp):  
  preamble = inp[i-PREAMBLE:i]
  check = inp[i]

  for j in range(0, len(preamble)):
    for k in range(0, len(preamble)-j):
      x = preamble[j]
      y = preamble[j+k]
      if x+y == check:
        return 0
  
  return check

def getInvalid(inp):
  for i in range(PREAMBLE, len(inp)):
    c = checkPreamble(i, input)
    if c > 0:
      return c
    i += 1
  return 0

answer = getInvalid(input)

print('ANSWER: ' + str(answer))