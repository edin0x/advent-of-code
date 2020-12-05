input = open("input", "r").read().split('\n')

valid = 0
for line in input:
  policy, password = line.split(': ')
  minString, part = policy.split('-')
  maxString, letter = part.split(' ')
  min = int(minString)
  max = int(maxString)

  count = password.count(letter)
  if min <= count and count <= max:
    valid = valid + 1

print(valid)