from collections import deque

def is_valid(matrix, x, y) -> bool:
  return False if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[x]) else True


def garden_walk_possibilities(grid: list[list[str]], start: tuple[int,int], steps: int) -> int:
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

  return len(list(possible_plots))

def part_one(inp: str, steps: int):
  grid = [[c for c in list(r)] for r in inp.splitlines()]
  start = None

  # Find start
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == 'S':
        start = (r,c)
  
  ans = garden_walk_possibilities(grid, start, steps)
        
  print('Answer 1 is:', ans)

# Explanation for Part 2

# Assumptions to check with input:
# Row and col at edges are all .
# Row and col with S (middle row/col) are all .
def check_assumptions(grid: list[list[str]], start: tuple[int,int], steps: int):
  assert len(grid) == len(grid[0])
  assert len(grid) % 2 == 1 and len(grid[0]) % 2 == 1

  # S is exactly in middle of grid ==> this also means # rows, # cols is odd
  assert start[0] == start[1] == len(grid) // 2

  # We can reach exactly the end of one grid going in one direction
  # This also means that we can not cover that last grid fully
  assert steps % len(grid) == len(grid) // 2

def part_two(inp: str, steps: int):
  grid = [[c for c in list(r)] for r in inp.splitlines()]
  start = None

  # Find start
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == 'S':
        start = (r,c)
  
  check_assumptions(grid, start, steps)
  
  ans = 0

  # How often do we repeat the grid going in one direction?
  grid_count = steps // len(grid) - 1 # -1 to discount initial grid

  # When we reach a repeated grid's S we can either have an even or odd number of steps left
  # Because grid width is odd, this alternates
  # => All directly adjacent grids to original will have even number left
  odd_grids = (grid_count // 2 * 2 + 1) ** 2
  even_grids = ((grid_count + 1) // 2 * 2) ** 2

  # Let's compute how many points we can reach on an odd grid (i.e. odd steps left) with sufficient steps (i.e. fully reachable grid)
  # We'll add these * our respective counts to the answer sum
  odd_reachable = garden_walk_possibilities(grid, start, len(grid) * 2 + 1)
  even_reachable = garden_walk_possibilities(grid, start, len(grid) * 2)
  ans += odd_grids * odd_reachable + even_grids * even_reachable

  # Now we handle the 4 final grids (u,r,d,l) that we can only partially walk because we don't have enough steps left to get to every point
  # This means we start at last row, first col, first row, last col (respectively) and have 1 fewer steps than size of grid left (because we reach end exactly)
  # We'll add these to the answer sum as is (we only have 4 of these)
  u_grid = garden_walk_possibilities(grid, (len(grid) - 1, start[1]), len(grid) - 1)
  r_grid = garden_walk_possibilities(grid, (start[0], 0), len(grid) - 1)
  d_grid = garden_walk_possibilities(grid, (0, start[1]), len(grid) - 1)
  l_grid = garden_walk_possibilities(grid, (start[0], len(grid[0]) - 1), len(grid) - 1)
  ans += u_grid + r_grid + d_grid + l_grid

  # Now we handle the corner sections of a grid we can reach from the edge grids, but where we can't get to that grid's S
  # We can't reach most points here
  # Each of those sections is repeated (grid_count + 1) times -> x*a + x*b ... = x * (a+b+...)
  # If we enter the top grid and go to its right (tr), we enter on the last row in the 1st col and so forth
  corner_tr = garden_walk_possibilities(grid, (len(grid) - 1, 0), len(grid) // 2 - 1)
  corner_tl = garden_walk_possibilities(grid, (len(grid) - 1, len(grid) - 1), len(grid) // 2 - 1)
  corner_br = garden_walk_possibilities(grid, (0, 0), len(grid) // 2 - 1)
  corner_bl = garden_walk_possibilities(grid, (0, len(grid) - 1), len(grid) // 2 - 1)
  ans += (grid_count + 1) * (corner_tr + corner_tl + corner_br + corner_bl)

  # Now we handle the subgrids, which are adjacent to those corners above and almost fully reachable but not the outmost corner
  # We can reach these from the edge-1'th grid => so we now have (3 * len(grid) // 2 - 1) steps left
  # These are repeated grid_count times
  subgrid_tr = garden_walk_possibilities(grid, (len(grid) - 1, 0), 3 * len(grid) // 2 - 1)
  subgrid_tl = garden_walk_possibilities(grid, (len(grid) - 1, len(grid) - 1), 3 * len(grid) // 2 - 1)
  subgrid_br = garden_walk_possibilities(grid, (0, 0), 3 * len(grid) // 2 - 1)
  subgrid_bl = garden_walk_possibilities(grid, (0, len(grid) - 1), 3 * len(grid) // 2 - 1)
  ans += grid_count * (subgrid_tr + subgrid_tl + subgrid_br + subgrid_bl)

  print('Answer 2 is:', ans)

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i, 64)
part_two(i, 26501365)