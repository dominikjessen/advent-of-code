import sys
import os
from itertools import product

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  schematics = inp.split('\n\n')

  locks = set()
  keys = set()

  for s in schematics:
    G = get_input_grid_char(s)

    pins = [0,0,0,0,0]
    for i, col in enumerate(zip(*G)):
      pins[i] = col.count('#') - 1

    if all(x == '#' for x in G[0]):
      locks.add(tuple(pins))
    else:
      keys.add(tuple(pins))

  s = 0
  combinations = list(product(locks, keys))
  for c in combinations:
    lock, key = c
    if all(a + b < 6 for a, b in zip(lock, key)):
      s += 1

  print('Answer 1 is:', s)


############
#  Part 2  #
############

def part_two(inp: str):
  print('Merry Christmas 🎄❤️')


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