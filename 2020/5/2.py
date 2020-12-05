import math
input = open("input", "r").read().split('\n')

ROWS = int(math.pow(2,7))
COLUMNS = 8
NUM_FIRST_PART = 7

def getSpot(bss, min, max):
  for bs in bss:
    half = int((max-min)/2 + 1)
    b = int(bs)
    min = min + (b^0)*half
    max = max - (b^1)*half
  
  return min

def getSeatID(bp):
  bs = bp.replace('F', '0').replace('B','1').replace('L','0').replace('R','1')

  row = getSpot(bs[:NUM_FIRST_PART], 0, ROWS-1)
  column = getSpot(bs[NUM_FIRST_PART:], 0, COLUMNS-1)

  return row*8 + column

def getMySeatID(seatIDs):
  minSeatID = min(seatIDs)
  for x in list(enumerate(sorted(seatIDs), start=minSeatID)):
    if x[0] != x[1]:
      return x[0]
  return -1

seatIDs = [getSeatID(bps) for bps in input]
mySeatID = getMySeatID(seatIDs)

print('ANSWER: ' + str(mySeatID))