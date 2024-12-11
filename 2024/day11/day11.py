import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *
from collections import defaultdict
from typing import DefaultDict

############
#  Part 1  #
############

def blink(stones: DefaultDict[str, int]) -> DefaultDict[str, int]:
  new_stones = defaultdict(int)

  for stone, count in stones.items():
    if stone == '0':
        new_stones['1'] += count
    elif len(stone) % 2 == 0:
      l,r =  stone[:len(stone)//2], stone[len(stone)//2:]
      r = str(int(r))

      new_stones[l] += count
      new_stones[r] += count
    else:
      new_stones[str(int(stone) * 2024)] += count

  return new_stones

def part_one(inp: str):
  # Get initial stones and their counts
  stones = defaultdict(int)

  for s in inp.split():
    stones[s] += 1
  
  for n in range(25):
    stones = blink(stones)

  print('Answer 1 is:', sum(stones.values()))


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
inp = open('./input.txt').read().strip()

# Solve example

print('Example 1')
print(40 * '=')

part_one(example1)
part_two(example1)

# print('\nExample 2')
# print(40 * '=')

# part_one(example2)
# part_two(example2)

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp)
# part_two(inp)