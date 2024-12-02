import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  r = get_input_rows(inp)
  minInc = 1
  maxInc = 3

  count = 0

  for (i, line) in enumerate(r):
    nums = line.split()
    nums = list(map(int, nums))

    inc = nums[0] - nums[1] < 0
    passes = 1

    for j in range(1, len(nums)):
      diff = nums[j] - nums[j-1]
      # Check directionality
      if (inc and diff < 0) or (not inc and diff > 0):
        passes = 0
        break

      # Check abs diff
      if abs(diff) < minInc or abs(diff) > maxInc:
        passes = 0
        break
  
    count += passes

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

# part_one(example)
part_two(example)

# Solve input

# print('\nSolution')
# print(40 * '=')

# part_one(inp)
# part_two(inp)