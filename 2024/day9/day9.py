import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  disc = []
  file_lengths = []
  free_lengths = []

  for i, num in enumerate(list(inp)):
    if i % 2 == 0:
      file_lengths.append(int(num))
    else:
      free_lengths.append(int(num))

  left_pointer = 0
  right_pointer = len(file_lengths) - 1
  free_pointer = 0
  writing_file = True

  while left_pointer <= right_pointer:
    if writing_file:
      while file_lengths[left_pointer] > 0:
        disc.append(left_pointer)
        file_lengths[left_pointer] -= 1
      
      writing_file = False
      left_pointer += 1
    else:
      if free_pointer >= len(free_lengths):
        continue

      while free_lengths[free_pointer] > 0:
        if file_lengths[right_pointer] > 0:
          disc.append(right_pointer)
          free_lengths[free_pointer] -= 1
          file_lengths[right_pointer] -= 1
        else:
          right_pointer -= 1

      writing_file = True
      free_pointer += 1

  s =  sum(i * num for i, num in enumerate(disc))
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