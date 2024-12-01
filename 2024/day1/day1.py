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
    l, r = row.split()
    l, r = int(l), int(r)

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
  r = inp.splitlines()
  s = 0

  left = []
  right_counts = dict()

  for (i, row) in enumerate(r):
    l, r = row.split()

    left.append(l)

    if r in right_counts:
      right_counts[r] += 1
    else:
      right_counts[r] = 1

  for (i, num) in enumerate(left):
    if num in right_counts:
      s += int(num) * right_counts[num]

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