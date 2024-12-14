import sys
import os
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  # This is just a system of linear equations with 2 unknowns
  s = 0

  machines = [x.split('\n') for x in inp.split('\n\n')]
  for m in machines:
    ax,ay = map(int, m[0].replace('Button A: X+', '').replace(', Y+', ',').split(','))
    bx,by = map(int, m[1].replace('Button B: X+', '').replace(', Y+', ',').split(','))
    px,py = map(int, m[2].replace('Prize: X=', '').replace(', Y=', ',').split(','))

    A = np.array([[ax, bx],[ay, by]])
    B = np.array([px, py])
    a,b = np.linalg.solve(A,B)

    # Account for floating point errors using numpy's built-in and check 100 heuristic we were given 
    if 0 <= a <= 100 and 0 <= b <= 100 and np.isclose(a,round(a)) and np.isclose(b,round(b)):
      s += 3 * a + b 

  print('Answer 1 is:', s)


############
#  Part 2  #
############

def part_two(inp: str):
    # This is just a system of linear equations with 2 unknowns
  s = 0

  machines = [x.split('\n') for x in inp.split('\n\n')]
  for m in machines:
    ax,ay = map(int, m[0].replace('Button A: X+', '').replace(', Y+', ',').split(','))
    bx,by = map(int, m[1].replace('Button B: X+', '').replace(', Y+', ',').split(','))
    px,py = map(int, m[2].replace('Prize: X=', '').replace(', Y=', ',').split(','))

    A = np.array([[ax, bx],[ay, by]])
    B = np.array([px, py]) + 10000000000000
    S = np.round(np.linalg.solve(A,B))

    # Verify solution with matrix multiplication
    if (B == S @ A.T).all():
      s += 3 * S[0] + S[1]
  
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