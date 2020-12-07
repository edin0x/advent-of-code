import math
input = open("input", "r").read().split('\n')
opcodes = list(map(int, ''.join(input).split(',')))

# restore gravity assist program
opcodes[1] = 12
opcodes[2] = 2

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

print(opcodes[0])