import sys
import os
import operator
import functools

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def move(sx: int, sy: int, vx: int, vy: int, mx: int, my: int):
  x,y = sx + vx, sy + vy

  if x > mx:
    x = x % mx - 1
  elif x < 0:
    x = mx + 1 + x

  if y > my:
    y = y % my - 1
  elif y < 0:
    y = my + 1 + y

  return (x,y)

def part_one(inp: str, max_x: int, max_y: int):
  quadrants = [0,0,0,0]

  robots = get_input_rows(inp)

  for robot in robots:
    p, v = robot.split()
    x, y = map(int, p.split('=')[1].split(','))
    vx, vy = map(int, v.split('=')[1].split(','))

    for i in range(100):
      x, y = move(x, y, vx, vy, max_x, max_y)
    
    if x < max_x / 2 and y < max_y / 2:
      quadrants[0] += 1
    elif x < max_x / 2 and y > max_y / 2:
      quadrants[1] += 1
    elif x > max_x / 2 and y < max_y / 2:
      quadrants[2] += 1
    elif x > max_x / 2 and y > max_y / 2:
      quadrants[3] += 1
    
  print('Answer 1 is:', functools.reduce(operator.mul, quadrants, 1))


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

print('Example')
print(40 * '=')

part_one(example, 10, 6)
part_two(example)

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp, 100, 102)
# part_two(inp)