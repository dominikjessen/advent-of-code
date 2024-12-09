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
  files = {}
  frees = []

  file_id = 0
  pos = 0

  # Find all files and non-empty blanks with positions and lengths
  for i, num in enumerate(list(inp)):
    l = int(num)
    if i % 2 == 0:
      if l == 0:
        raise ValueError('unexpected 0 length for file')
      
      files[file_id] = (pos, l)
      file_id += 1
    else:
      if l != 0:
        frees.append((pos, l))
    
    pos += l
  
  # Build our moved file positions in the dict
  while file_id > 0:
    file_id -= 1
    file_pos, file_size = files[file_id]

    for i, (free_pos, free_size) in enumerate(frees):
      # We have tried all free positions for this file and any free space to the right is irrelevant for us from here
      if free_pos >= file_pos:
        frees = frees[:i]
        break
      
      # Move the file if space and handle remaining free space
      if file_size <= free_size:
        files[file_id] = (free_pos, file_size)

        # File fits free space exactly --> remove free space from future contention
        # Else adjust starting pos for free space and length of remaining free space by file_size
        if file_size == free_size:
          frees.pop(i)
        else:
          frees[i] = (free_pos + file_size, free_size - file_size)
        
        break

  s = 0
  for f_id, (start, size) in files.items():
    for x in range(start, start + size):
      s += x * f_id

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