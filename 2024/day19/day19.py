import sys
import os
from functools import cache

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  t,d = inp.split('\n\n')
  t = set(t.split(', '))
  largest_t = max(map(len, t))
  d = d.splitlines()  

  # Check longest possible towel first, then see if remaining towel design is possible
  # Recurse and check smaller towels until no towel works (False) or design is made (True)
  # Needs memoization to run in time (sub-designs of designs will always have the same answer)
  @cache
  def design_possible(d: str) -> bool:
    if d == '':
      return True
    
    for i in range(min(len(d), largest_t) + 1):
      if d[:i] in t and design_possible(d[i:]):
        return True
      
    return False

  s = 0
  for design in d:
    s += design_possible(design)

  print('Answer 1 is:', s)


############
#  Part 2  #
############

def part_two(inp: str):
  t,d = inp.split('\n\n')
  t = set(t.split(', '))
  largest_t = max(map(len, t))
  d = d.splitlines()  

  # We count all arrangements this time instead of possible/not possible. If not possible count will stay at 0
  @cache
  def ways_design_possible(d: str) -> int:
    if d == '':
      return 1
    
    count = 0
    
    for i in range(min(len(d), largest_t) + 1):
      if d[:i] in t:
        count += ways_design_possible(d[i:])
      
    return count

  print('Answer 2 is:', sum(ways_design_possible(design) for design in d))


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