from collections import deque
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

dirs = {
  '^': (-1,0),
  '>': (0,1),
  'v': (1,0),
  '<': (0,-1)
}

def part_one(inp: str):
  # Find start
  g, moves = inp.split('\n\n')
  moves = [m for ms in moves for m in ms if m != '\n']

  G = get_input_grid_char(g)
  rows = len(G)
  cols = len(G[0])

  # Start at (r,c) for robot
  for r in range(rows):
    for c in range(cols):
      if G[r][c] == '@':
        break
    else:
      continue
    break

  # Process all moves
  for move in moves:
    dr,dc = dirs[move]
    cr,cc = r, c
    boxes = []
    moving = True

    # Accumulate boxes while pushing things if we encounter them
    while True:
      cr,cc = cr + dr, cc + dc  
      if G[cr][cc] == '#':
        moving = False
        break

      if G[cr][cc] == '.':
        break

      if G[cr][cc] == 'O':
        boxes.append((cr,cc))

    # If we cannot move we just keep going, else we update robot and all boxes and move our robot
    if not moving:
      continue

    G[r][c] = '.'
    G[r+dr][c+dc] = '@'

    for br,bc in boxes:
      G[br+dr][bc+dc] = 'O'

    r,c = r+dr,c+dc

  s = 0
  for r in range(rows):
    for c in range(cols):
      if G[r][c] == 'O':
        s += 100 * r + c

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