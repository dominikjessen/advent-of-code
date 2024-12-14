import sys
import os
import operator
import functools
from PIL import Image, ImageDraw

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

def make_grid_image(G: List[List[str]], i: int):
  cell_size = 10
  width = len(G[0]) * cell_size
  height = len(G) * cell_size

  # Create black background image
  img = Image.new('RGB', (width, height), color = (0, 0, 0))
  draw = ImageDraw.Draw(img)

  # Fill robots white
  for y, row in enumerate(G):
      for x, char in enumerate(row):
          if char != '':
              draw.rectangle([(x * cell_size, y * cell_size), ((x + 1) * cell_size - 1, (y + 1) * cell_size - 1)], fill=(255, 255, 255))

  img.save(os.path.join('./images', f"0000{i}grid.bmp"))

def part_two(inp: str, max_x: int, max_y: int):
  r = get_input_rows(inp)
  robots = []
  velocities = []

  # Get robot start positions
  for line in r:
      p, v = line.split()
      x, y = map(int, p.split('=')[1].split(','))
      vx, vy = map(int, v.split('=')[1].split(','))
      robots.append((x,y))
      velocities.append((vx,vy))
  
  # Start moving robots
  for i in range(2):
    G = [['' for x in range(max_x + 1)] for y in range(max_y + 1)]
    for j in range(len(robots)):
      x,y = robots[j]
      vx,vy = velocities[j]
      x,y = move(x, y, vx, vy, max_x, max_y)
      robots[j] = (x,y)
      G[y][x] = 'X'

    # Make an image
    make_grid_image(G, i)

#############
#  Solving  #
#############

# Input
example = open('./example.txt').read().strip()
inp = open('./input.txt').read().strip()

print('Example')
print(40 * '=')

part_one(example, 10, 6)
# part_two(example, 10, 6)

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp, 100, 102)
part_two(inp, 100, 102)