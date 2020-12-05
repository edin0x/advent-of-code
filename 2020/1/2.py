input = open("input", "r").read().split('\n')
numbers = [int(x) for x in input]

n = len(numbers)
for i in range(n-1):
  testAgainst = numbers[i+1:n]
  for j in range(n-i):
    for k in range(n-i-j):
      sum = numbers[i] + numbers[i+j] + numbers[i+j+k]
      if sum == 2020:
        print('SUM: ' + str(numbers[i]) + ' + ' + str(numbers[i+j]) + ' + ' + str(numbers[i+j+k]) + ' = ' + str(sum))
        print('ANSWER: ' + str(numbers[i]*numbers[i+j]*numbers[i+j+k]))