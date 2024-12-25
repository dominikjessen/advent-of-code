from math import floor
import sys
import os
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def transform_num(n: int) -> int:
  n = (n ^ (n * 64)) % 16777216
  n = (n ^ (n // 32)) % 16777216
  n = (n ^ (n * 2048)) % 16777216

  return n

def part_one(inp: str):
  nums = list(map(int, get_input_rows(inp)))

  s = 0
  for n in nums:
    for _ in range(2000):
      n = transform_num(n)
    s += n

  print('Answer 1 is:', s)


############
#  Part 2  #
############

def part_two(inp: str):
  nums = list(map(int, get_input_rows(inp)))

  sequences = {}

  for n in nums:
    prices = [n % 10]
    for _ in range(2000):
      n = transform_num(n)
      prices.append(n % 10)
  
    seen = set()
    for i in range(len(prices) - 4):
      a,b,c,d,e = prices[i:i+5]
      diffs = (b-a, c-b, d-c, e-d)

      if diffs in seen:
        continue

      seen.add(diffs)

      if diffs not in sequences: 
        sequences[diffs] = 0

      sequences[diffs] += e

  print('Answer 2 is:', max(sequences.values()))


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