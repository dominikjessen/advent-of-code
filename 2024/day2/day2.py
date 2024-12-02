import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def is_valid(nums: List[int], minI: int, maxI: int) -> bool:
  diffs = [a - b for a, b in zip(nums, nums[1:])]
  return all(minI <= a <= maxI for a in diffs) or all(-maxI <= a <= -minI for a in diffs)

def part_one(inp: str):
  r = get_input_rows(inp)
  count = 0

  for line in r:
    nums = line.split()
    nums = list(map(int, nums))

    if is_valid(nums, 1, 3):
      count += 1

  print('Answer 1 is:', count)


############
#  Part 2  #
############

def part_two(inp: str):
  r = get_input_rows(inp)
  count = 0

  for line in r:
    nums = line.split()
    nums = list(map(int, nums))

    # Test if removing any index leads to safe row
    if any(is_valid(nums[:i] + nums[i+1:], 1, 3) for i in range(len(nums))):
      count += 1

  print('Answer 2 is:', count)


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