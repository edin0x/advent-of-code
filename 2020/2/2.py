input = open("input", "r").read().split('\n')

valid = 0
for line in input:
  policy, password = line.split(': ')
  firstNumberString, part = policy.split('-')
  secondNumberString, letter = part.split(' ')
  firstNumber = int(firstNumberString)
  secondNumber = int(secondNumberString)

  if (password[firstNumber-1] == letter) ^ (password[secondNumber-1] == letter):
    valid = valid + 1

print(valid)