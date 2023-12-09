from typing import List

def build_history(row: List[int]) -> List[List[int]]:
  history = []
  history.append(row)

  i = 0
  while True:
    nextRow = []
    for j in range(1,len(history[i])):
      nextRow.append(history[i][j]-history[i][j-1])
      
    history.append(nextRow)
    # Input has negative numbers, so can't just check sum of row
    if all(i == 0 for i in nextRow):
      return history
    i += 1
  
# Create a copy of history with extrapolated value at end
# NOTE: because of append via list concatenation a shallow copy suffices. With .append() use copy.deepcopy()
def extrapolate_history_end(history: List[List[int]]) -> List[List[int]]:
  extrapolated = history[:]
  n = len(extrapolated)-1
  while n >= 0:
    if n == len(extrapolated)-1:
      extrapolated[n] = extrapolated[n] + [0]
    else:
      nextVal = extrapolated[n+1][-1] + extrapolated[n][-1]
      extrapolated[n] = extrapolated[n] + [nextVal]
    n -= 1
  
  return extrapolated

# Create a copy of history with extrapolated value at front
# NOTE: because of append via list concatenation a shallow copy suffices.
def extrapolate_history_front(history: List[List[int]]) -> List[List[int]]:
  extrapolated = history[:]
  n = len(extrapolated)-1
  while n >= 0:
    if n == len(extrapolated)-1:
      extrapolated[n] = [0] + extrapolated[n]
    else:
      firstVal = extrapolated[n][0] - extrapolated[n+1][0]
      extrapolated[n] = [firstVal] + extrapolated[n]
    n -= 1
  
  return extrapolated

def part_one(inp: str):
  # Build histories
  histories = []
  for line in inp.splitlines():
    base_row = [int(x) for x in line.strip().split()]
    histories.append(build_history(base_row))

  s = 0
  for history in histories:
    extrapolated = extrapolate_history_end(history)
    s += extrapolated[0][-1]

  print('Answer 1 is:', s)

def part_two(inp: str):
  # Build histories
  histories = []
  for line in inp.splitlines():
    base_row = [int(x) for x in line.strip().split()]
    histories.append(build_history(base_row))

  s = 0
  for history in histories:
    extrapolated = extrapolate_history_front(history)
    s += extrapolated[0][0]

  print('Answer 2 is:',s)
  

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
part_two(i)