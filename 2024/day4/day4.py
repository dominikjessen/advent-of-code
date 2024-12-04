import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  G = get_input_grid_char(inp)
  count = 0

  for r in range(len(G)):
    for c in range(len(G[r])):
      if G[r][c] == 'X':
        dirs = get_adjacent_coords(0,0,True)
        coords = get_adjacent_coords(r,c,True)

        while coords:
          mr,mc = coords.pop()
          dr,dc = dirs.pop()

          if is_valid_move(G, mr, mc) and G[mr][mc] == 'M':
            ar = mr + dr
            ac = mc + dc

            if is_valid_move(G, ar, ac) and G[ar][ac] == 'A':
              sr = ar + dr
              sc = ac + dc

              if is_valid_move(G, sr, sc) and G[sr][sc] == 'S':
                count += 1

  print('Answer 1 is:', count)


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