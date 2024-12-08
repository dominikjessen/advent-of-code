import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *
from itertools import combinations

############
#  Part 1  #
############

def get_antinode_positions(G: List[List[str]], nodes: List[Tuple[int,int]]) -> Set[Tuple[int,int]]:
  pairs = combinations(nodes, 2)
  antinodes = set()

  for p in pairs:
    p1,p2 = p
    d1,d2 = p2[0] - p1[0], p2[1] - p1[1]
    
    # Get two antinodes for pair and add to set if valid for grid
    a1 = ( p1[0] - d1, p1[1] - d2)
    a2 = ( p2[0] + d1, p2[1] + d2)

    if is_valid_move(G, a1[0], a1[1]):
      antinodes.add(a1)
    
    if is_valid_move(G, a2[0], a2[1]):
      antinodes.add(a2)

  return antinodes

def part_one(inp: str):
  G = get_input_grid_char(inp)

  antennas = {}
  antinodes = set()

  # Find all positions per antenna type
  for r in range(len(G)):
    for c in range(len(G[r])):
      if G[r][c] != '.':
        if G[r][c] not in antennas:
          antennas[G[r][c]] = []

        antennas[G[r][c]].append((r,c))

  # Find all antinodes and do a set union
  for v in antennas.values():
    k_antinodes = get_antinode_positions(G, v)
    antinodes |= k_antinodes

  print('Answer 1 is:', len(antinodes))


############
#  Part 2  #
############

def part_two(inp: str):
  print('Answer 2 is:')


#############
#  Solving  #
#############

# Input
example1 = open('./example1.txt').read().strip()
example2 = open('./example2.txt').read().strip()
example3 = open('./example3.txt').read().strip()

inp = open('./input.txt').read().strip()

# Solve example

print('Example 1')
print(40 * '=')

part_one(example1)
part_two(example1)

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp)
# part_two(inp)