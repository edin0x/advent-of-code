input = open("input", "r").read().split('\n')

def findExit(instructions, acc):
  visited = [0 for i in range(0, len(input))]

  i = 0
  acc = 0
  previousI = 0
  while True:
    if i == len(instructions):
      return acc
    elif visited[i] == 1:
      return 0

    visited[previousI] = 1
    previousI = i
    ci, val = instructions[i]

    if ci == 'nop':
      i += 1
    elif ci == 'acc':
      acc += int(val)
      i += 1
    elif ci == 'jmp':
      i += int(val)
  
  return acc

def findWorkingAcc(fperm, bperm):
  if bperm == []:
    return 0

  iv = bperm[0]
  fperm_original = fperm.copy()
  a = 0
  if iv[0] == 'jmp':
    fperm = fperm + [['nop',iv[1]]]
  elif iv[0] == 'nop':
    fperm = fperm + [['jmp',iv[1]]]

  a = findExit(fperm + bperm[1:], 0)
  if a > 0:
    return a

  return findWorkingAcc(fperm_original + [iv], bperm[1:])
  
instructions = [ins.split(' ') for ins in input]
answer = findWorkingAcc([], instructions)

print('ANSWER: ' + str(answer))