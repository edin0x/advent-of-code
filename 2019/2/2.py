import math
input = open("input", "r").read().split('\n')
opcodes = list(map(int, ''.join(input).split(',')))

def calculateOpcode(opcodes):
  i = 0
  while True:
    if opcodes[i] == 99:
      break

    if opcodes[i] == 1:
      opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] + opcodes[opcodes[i+2]]
    elif opcodes[i] == 2:
      opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] * opcodes[opcodes[i+2]]
    else:
      print(opcodes[i])
      print('Something went wrong.')
      break

    i += 4
  return opcodes

def getNounVerbForOutput(opcodes, output):
  original_opcodes = opcodes.copy()
  for noun in range(0,100):
    for verb in range(0,100):
      opcodes[1] = noun
      opcodes[2] = verb

      opcodes = calculateOpcode(opcodes)
      if opcodes[0] == output:
        return noun, verb

      opcodes = original_opcodes.copy()
  
  print('No noun/verb found.')

noun, verb = getNounVerbForOutput(opcodes, 19690720)

print('ANSWER: ' + str(100*noun + verb))
