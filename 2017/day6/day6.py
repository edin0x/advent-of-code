import operator

INPUT = [10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6]
l = len(INPUT)
seen_states = []

state = INPUT[:]
seen_states.append(INPUT[:])
steps = 0
while True:
  maxValueIndex, maxValue = max(enumerate(state), key=operator.itemgetter(1))
  state[maxValueIndex] = 0
 
  i = maxValueIndex + 1
  for _ in range(maxValue):
    state[i%l] += 1
    i += 1
  
  steps += 1
  if state in seen_states:
    print "Answer part 1: ", steps
    print "Answer part 2: ", steps - seen_states.index(state)
    break;
  else:
    seen_states.append(state[:])
