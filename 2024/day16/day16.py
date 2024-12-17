import copy
import heapq
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  # Dijkstra the shortest path --> potentially just do this because building graph might be expensive
  
  G = get_input_grid_char(inp)
  rows = len(G)
  cols = len(G[0])
  start = ()
  end = ()

  for r in range(rows):
    for c in range(cols):
      if G[r][c] == 'S':
        start = (r,c)
      elif G[r][c] == 'E':
        end = (r,c)
  
  scores = {}
  seen = set()

  # Start facing east
  pq = [(0, start[0], start[1], 0, 1)]

  while pq:
    curr_score, r, c, cdr, cdc = heapq.heappop(pq)

    if not (r,c) in scores:
      scores[(r,c)] = curr_score
    elif scores[(r,c)] > curr_score:
      scores[(r,c)] = curr_score

    if (r,c,cdr,cdc) in seen:
      continue
    
    seen.add((r,c,cdr,cdc))

    valid_dirs = set([(-1, 0), (0, 1), (1, 0), (0, -1)])
    # Can't turn around so remove that direction from valid
    valid_dirs.remove((-cdr, -cdc))

    for (dr,dc) in valid_dirs:
      if G[r+dr][c+dc] == '#':
        continue

      if dr == cdr and dc == cdc:
        heapq.heappush(pq, ( curr_score + 1, r + dr, c + dc, dr, dc))
      else:
        heapq.heappush(pq, ( curr_score + 1001, r + dr, c + dc, dr, dc)) # Just turn

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
example2 = open('./example2.txt').read().strip()
inp = open('./input.txt').read().strip()

# Solve example

print('Example')
print(40 * '=')

part_one(example)
part_one(example2)
# part_two(example)

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp)
# part_two(inp)