from collections import deque

def is_valid(matrix, x, y) -> bool:
  return False if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[x]) else True

def part_one(inp: str, steps: int):
  grid = [[c for c in list(r)] for r in inp.splitlines()]
  start = None

  # Find start
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == 'S':
        start = (r,c)
        
  possible_plots = set()
  seen = {(start[0],start[1])}

  queue = deque() # r,c,steps so far
  queue.append((start[0], start[1], steps))

  while queue:
    r,c,steps_left = queue.popleft()

    # If we have even steps left, just walk back and forth
    if steps_left % 2 == 0:
      possible_plots.add((r,c))
      
    # No more steps left, went too far out
    if steps_left <= 0:
      continue

    # u, r, d, l
    DR = [-1,0,1,0]
    DC = [0,1,0,-1]
    for i in range(4):
      dr = r + DR[i]
      dc = c + DC[i]

      # If valid new, non-rock node, append it with one fewer steps left
      if is_valid(grid, dr,dc) and grid[dr][dc] != '#' and (dr,dc) not in seen:
        seen.add((dr,dc))
        queue.append((dr,dc,steps_left-1))

  print('Answer 1 is:', len(list(possible_plots)))
  pass

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i, 64)
# part_two(i)