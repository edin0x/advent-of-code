input = open("input", "r").read().split('\n\n')

count = 0
for line in input:
  groupAnswers = line.split('\n')
  answerSet = set(''.join(groupAnswers))
  count = count + sum([all([a in ga for ga in groupAnswers]) for a in answerSet])

print('ANSWER: ' + str(count))