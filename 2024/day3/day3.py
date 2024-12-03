import sys
import os
import re
import operator
import functools

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def mul_sum(inp: str) -> int:
  matches = re.findall('mul\(\d{1,3},\d{1,3}\)', inp)
  s = 0
  for m in matches:
    s += functools.reduce(operator.mul, map(int,  m[4:-1].split(',')), 1)
  
  return s

def part_one(inp: str):
  print('Answer 1 is:', mul_sum(inp))


############
#  Part 2  #
############

def part_two(inp: str):
  test_str = ''
  dos = inp.split("do()")

  for d in dos:
    test_str += d.split("don't()")[0]

  print('Answer 2 is:', mul_sum(test_str))


#############
#  Solving  #
#############

# Input
example = open('./example.txt').read().strip()
example2 = open('./example2.txt').read().strip()
inp = open('./input.txt').read().strip()

# Solve example

print('Example')
print(40 * '=')

part_one(example)
part_two(example2)

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp)
part_two(inp)