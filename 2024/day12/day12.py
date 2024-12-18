import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

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

def get_component_sides(G: List[List[int]], comps: Set[Tuple[int,int]]) -> int:
  # Build edges between garden cells first (i.e. fence pieces) which have an orientation toward their garden (think: walls)
  edges = {}

  for r,c in comps:
    for nr,nc in get_adjacent_coords(r,c):
      if (nr,nc) in comps:
        continue
        
      er = (r + nr) / 2
      ec = (c + nc) / 2
      edges[(er, ec)] = (er - r, ec - c)
  
  # Adjacent fence pieces with the same direction in respect to the garden they surround are one side
  seen = set()
  sides = 0

  for edge, e_dir in edges.items():
    if edge in seen:
      continue

    seen.add(edge)
    sides += 1

    er, ec = edge

    # Advance forward with our side edge or other edges by stepping until direction change
    if er % 1 == 0:
      for dr in [-1,1]:
        cr = er + dr
        while edges.get((cr, ec)) == e_dir:
          seen.add((cr, ec))
          cr += dr
    else:
      for dc in [-1,1]:
        cc = ec + dc
        while edges.get((er, cc)) == e_dir:
          seen.add((er, cc))
          cc += dc
  return sides

def part_two(inp: str):
  G = get_input_grid_char(inp)
  components = []

  # Make sure to have new entry points for stack after exhausting component
  unvisited = set()
  for r in range(len(G)):
    for c in range(len(G[r])):
      unvisited.add((r,c))
  
  # Get connected components and their coords
  stack = []
  stack.append((0, 0, G[0][0], set()))
  seen = set()

  while stack:
    r, c, char, component_parts = stack.pop()

    # We've found the end of a garden plot, add it to components and restart if still unvisited cells left
    if not stack:
      components.append(component_parts)
  
      if unvisited:
        ur,uc = unvisited.pop()
        stack.append((ur,uc, G[ur][uc], set()))

    if (r,c) in seen:
      continue

    unvisited.discard((r,c))
    component_parts.add((r,c))
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
      sides = get_component_sides(G, comps)
      
      s += len(comps) * sides

  print('Answer 2 is:', s)


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
part_two(inp)