import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  lines = get_input_rows(inp)
  s = 0

  for l in lines:
    sol, nums = l.split(':')
    sol = int(sol)
    nums = [int(x) for x in nums.split()]

    stack = []
    stack.append((nums[0], 1))

    while stack:
      curr, i = stack.pop()

      if curr == sol and i == len(nums):
        s += sol
        break

      if i == len(nums):
        continue

      stack.append((curr + nums[i], i+1))
      stack.append((curr * nums[i], i+1))

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