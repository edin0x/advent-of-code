import re
input = open("input", "r").read().split('\n')

instructions = [ins.split(' ') for ins in input]
visited = [0 for i in range(0, len(input))]

i = 0
acc = 0
previousI = 0
while True:
  if visited[i] == 1 or i == len(instructions):
    break

  visited[previousI] = 1
  previousI = i
  ci, val = instructions[i]

  print(ci, val)
  if ci == 'nop':
    i += 1
  elif ci == 'acc':
    acc += int(val)
    i += 1
  elif ci == 'jmp':
    i += int(val)
  
  print(acc, visited)

answer = acc

print('ANSWER: ' + str(answer))