import math
input = open("input", "r").read().split('\n')
masses = [int(x) for x in input]

fuels = [int(int(m)/3)-2 for m in masses]

answer = sum(fuels)
print ('ANSWER: ' + str(answer))