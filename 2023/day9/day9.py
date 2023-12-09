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
  
def part_one(inp: str):
  # Build histories
  histories = []
  for line in inp.splitlines():
    base_row = [int(x) for x in line.strip().split()]
    histories.append(build_history(base_row))

  s = 0
  for history in histories:
    n = len(history)-1
    while n >= 0:
      if n == len(history)-1:
        history[n].append(0)
      else:
        nextVal = history[n+1][-1] + history[n][-1]
        history[n].append(nextVal)
      n -= 1
    s += history[0][-1]

  print('Answer 1 is:', s)


# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)