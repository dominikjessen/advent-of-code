import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  G = get_input_grid_char(inp)

  curr = ()
  curr_dir_i = 0

  directions = [
    (-1, 0),  # Up
    (0, 1),   # Right
    (1, 0),   # Down
    (0, -1),  # Left
  ]

  visited = set()

  for r in range(len(G)):
    for c in range(len(G[r])):
      if G[r][c] == '^':
        curr = (r, c)
        visited.add((r,c))
  
  
  while is_valid_move(G, curr[0], curr[1]):
    dr,dc = directions[curr_dir_i]
    nr,nc = curr[0] + dr, curr[1] + dc

    if not is_valid_move(G, nr, nc):
      break

    if G[nr][nc] == '#':
      curr_dir_i = (curr_dir_i + 1) % len(directions)
      continue

    if not (nr,nc) in visited:
      G[nr][nc] = '@'
      visited.add((nr,nc))

    curr = (nr,nc)
  
  print('Answer 1 is:', len(visited))


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