input = open("input", "r").read().split('\n\n')

sum = sum([len(set(line.replace('\n', ''))) for line in input])

print('ANSWER: ' + str(sum))