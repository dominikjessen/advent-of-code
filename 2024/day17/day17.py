import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  combo_operands = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": "A", # Register value
    "5": "B", # Register value
    "6": "C"  # Register value
  }

  r,p = inp.split('\n\n')
  p = p.split(': ')[1].split(',')

  for i, rg in enumerate(r.splitlines()):
    combo_operands[str(i+4)] = int(rg.split(': ')[1])

  out = []
  i = 0
  while i < len(p):
    ins = p[i]
    op = p[i+1]

    match ins:
      case "0":
        combo_operands["4"] = int(combo_operands["4"] / 2 ** combo_operands[op])
      case "1":
        combo_operands["5"] ^= int(op)
      case "2":
        combo_operands["5"] = combo_operands[op] % 8
      case "3":
        i = i if combo_operands["4"] == 0 else int(op) - 2 
      case "4":
        combo_operands["5"] ^= combo_operands["6"]
      case "5":
        out.append(combo_operands[op] % 8)
      case "6":
        combo_operands["5"] = int(combo_operands["4"] / 2 ** combo_operands[op])
      case "7":
        combo_operands["6"] = int(combo_operands["4"] / 2 ** combo_operands[op])

    i += 2

  print('Answer 1 is:', ','.join(str(x) for x in out))


############
#  Part 2  #
############

def find(program: List[int], solution: int) -> int:
  if program == []:
    return solution >> 3 # See below...
  
  # My program until out()
  for x in range(8):
    a = solution + x

    b = a % 8
    b ^= 3
    c = a >> b
    b ^= 5
    a <<= 3 # This is happening in my final loop going up, so reserve it for answer
    b ^= c

    if b % 8 == program[-1]:
      s = find(program[:-1], a)
      if s == None:
        continue

      return s
    
def part_two(inp: str):
  _,p = inp.split('\n\n')
  p = list(map(int,p.split(': ')[1].split(',')))
  print('Answer 2 is:', find(p, 0))


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

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp)
part_two(inp)