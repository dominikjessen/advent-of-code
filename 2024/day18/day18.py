import sys
import os
import heapq

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str, grid_size: int, num_bytes_falling: int):
  G = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

  for r in get_input_rows(inp)[:num_bytes_falling]:
    x,y = map(int, r.split(','))
    G[y][x] = '#'
  
  # Find path from start to end
  start = (0,0)
  end = (grid_size - 1, grid_size - 1)

  scores = {}
  seen = set()

  pq = [(0, start[0], start[1], 0, 1)]

  while pq:
    curr_steps, r, c, cdr, cdc = heapq.heappop(pq)

    if not (r,c) in scores:
      scores[(r,c)] = curr_steps
    elif scores[(r,c)] > curr_steps:
      scores[(r,c)] = curr_steps

    if (r,c) == end:
      break

    if (r,c,cdr,cdc) in seen:
      continue
    
    seen.add((r,c,cdr,cdc))

    for (dr,dc) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
      if not is_valid_move(G, r+dr, c+dc) or G[r+dr][c+dc] == '#':
        continue

      heapq.heappush(pq, ( curr_steps + 1, r + dr, c + dc, dr, dc))

  print('Answer 1 is:', scores[end])

############
#  Part 2  #
############

def part_two(inp: str):
  print('Answer 2 is:')


#############
#  Solving  #
#############

# Input
example = open('./example.txt').read().strip()
inp = open('./input.txt').read().strip()

# Solve example

print('Example')
print(40 * '=')

part_one(example, 7, 12)
part_two(example)

# Solve input

# print('\nSolution')
# print(40 * '=')

part_one(inp, 71, 1024)
# part_two(inp)