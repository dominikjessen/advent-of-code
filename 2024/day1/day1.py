import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  r = get_input_rows(inp)
  s = 0

  left = []
  right = []

  for (i, row) in enumerate(r):
    # Parse numbers
    l = int(row[0:5])
    r = int(row[-5:])

    left.append(l)
    right.append(r)

  left.sort()
  right.sort()

  for i in range(len(left)):
    s += abs(left[i] - right[i])

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
# part_two(example)

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp)
# part_two(inp)