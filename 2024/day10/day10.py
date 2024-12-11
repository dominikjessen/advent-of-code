import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  G = get_input_grid_int(inp)

  trail_heads = []

  rows = len(G)
  cols = len(G[0])

  # Get all trail_heads
  for r in range(rows):
    for c in range(cols):
      if G[r][c] == 0:
        trail_heads.append((r,c, 0))
  
  # Explore all trail_heads for their hiking score
  s = 0

  for t in trail_heads:
    # We're looking for unique peaks not different ways of reaching the same peak, so set instead of counter
    peaks = set()
    stack = [t]

    while stack:
      r,c,height = stack.pop()

      # Found trail end, stop exploring this path
      if height == 9:
        peaks.add((r,c))
        continue

      # Add next valid moves (neighbor, valid grid move, and height of curr_h + 1)
      for nr,nc in get_adjacent_coords(r,c):
        if is_valid_move(G, nr,nc) and G[nr][nc] == height + 1:
          stack.append((nr,nc, G[nr][nc]))

    s += len(peaks)

  print('Answer 1 is:', s)


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

part_one(example)
part_two(example)

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp)
# part_two(inp)