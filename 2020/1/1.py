input = open("input", "r").read().split('\n')
numbers = [int(x) for x in input]

n = len(numbers)
for i in range(n-1):
  testAgainst = numbers[i+1:n]
  for j in range(n-i):
    sum = numbers[i] + numbers[i+j]
    if sum == 2020:
      print('SUM: ' + str(numbers[i]) + ' + ' + str(numbers[i+j]) + ' = ' + str(sum))
      print ('ANSWER: ' + str(numbers[i]*numbers[i+j]))