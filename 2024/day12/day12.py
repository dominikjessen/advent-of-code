import sys
import os
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def shoelace_area(x, y) -> int:
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def get_cell_perimeter(G: List[List[str]], cell: Tuple[int,int]) -> int:
  p = 4
  x,y = cell
  neighbors = get_adjacent_coords(x, y)

  for nr,nc in neighbors:
    if is_valid_move(G, nr, nc) and G[nr][nc] == G[x][y]:
      p -= 1

  return p

def part_one(inp: str):
  G = get_input_grid_char(inp)
  components = []

  # Make sure to have new entry points for stack after exhausting component
  unvisited = set()
  for r in range(len(G)):
    for c in range(len(G[r])):
      unvisited.add((r,c))
  
  # Get connected components and their coords
  stack = []
  stack.append((0, 0, G[0][0], []))
  seen = set()

  while stack:
    r, c, char, component_parts = stack.pop()

    # We've found the end of a garden plot, add it to components and restart if still unvisited cells left
    if not stack:
      components.append(component_parts)
  
      if unvisited:
        ur,uc = unvisited.pop()
        stack.append((ur,uc, G[ur][uc], []))

    if (r,c) in seen:
      continue

    unvisited.discard((r,c))
    component_parts.append((r,c))
    seen.add((r,c))

    directions = [
        (-1, 0),  # Up
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
    ]

    for dr,dc in directions:
      # Only visit cells that have same type of flower
      if not is_valid_move(G, r + dr, c + dc) or G[r + dr][c + dc] != char:
        continue

      stack.append((r + dr, c + dc, G[r + dr][c + dc], component_parts))

  # Calculate total with individual area * perimeters for each connected component
  s = 0
  for comps in components:
    if comps != []:
      perimeter = 0

      for cell in comps:
        perimeter += get_cell_perimeter(G, cell)
      
      s += len(comps) * perimeter

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