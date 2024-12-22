import sys
import os
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  G = get_input_grid_char(inp)

  sr, sc = 0, 0

  for r in range(len(G)):
    for c in range(len(G[r])):
      if G[r][c] == 'S':
        sr,sc = r,c

  # Build track with positions
  stack = []
  track = {}
  stack.append((sr,sc, 1))

  while stack:
    r,c,secs = stack.pop()

    if (r,c) in track:
      continue

    track[(r,c)] = secs

    neighbors = get_adjacent_coords(r,c)
    for nr,nc in neighbors:
      if G[nr][nc] != '#':
        stack.append((nr,nc,secs + 1))

  # Rerun through track but check cheating now
  stack.append((sr,sc, 1))
  seen = set() # This is just for the second pass
  cheats = defaultdict(int)

  while stack:
    r,c,secs = stack.pop()

    if (r,c) in seen:
      continue

    dirs =  [
      (-1, 0),
      (0, 1),
      (1, 0),
      (0, -1),
  ]
    for dr,dc in dirs:
      # Get the cheat savings
      if G[r+dr][c+dc] == '#':
        if (r + 2 * dr, c + 2 * dc) in track:
          savings = track[(r + 2 * dr, c + 2 * dc)] - secs - 2 # -2 because we do have to spend 2 picoseconds to move there with the cheat
          cheats[savings] += 1

      # Go to next track position
      elif track[(r+dr,c+dc)] > secs:
        stack.append((r+dr,c+dc,secs + 1))

  s = sum(v for k, v in cheats.items() if k >= 100)
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