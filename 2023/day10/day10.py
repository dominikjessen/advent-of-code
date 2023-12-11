# Tricky part here is to remember to switch directions when curved pipe is encountered
# NOTE: Because input only has 2 possible paths from S (i.e. both sides of same loop), just walk along one until back to S. 
# NOTE: Else, would have to follow one path first until impossible move
from collections import deque


def part_one(inp: str):
  grid = []
  MOVES = {'n': (-1,0), 'e': (0,1), 's':(1,0), 'w':(0,-1)}

  # Build grid and find S
  start = ()
  for i,line in enumerate(inp.splitlines()):
    row = []
    for j,c in enumerate(list(line)):
      if c == 'S':
        start = (i,j)
      row.append(c)
    grid.append(row)

  valid_chars_for_direction = {'n': ['|','7','F'], 'e': ['-','J','7'], 's': ['|','L','J'], 'w': ['-','L','F'],}
  first_moves = []
  for direction,move in MOVES.items():
    path_char = grid[start[0]+move[0]][start[1]+move[1]]
    valid_move = path_char in valid_chars_for_direction[direction]
    if valid_move:
      first_moves.append((direction,(start[0]+move[0],start[1]+move[1])))
    
  # We're starting at one of the first moves and break when we find S again. That's why our initial distance is 1.
  c = first_moves.pop()
  dist = 1
  while True:
    row = c[1][0]
    col = c[1][1]
    direction = c[0]
    char = grid[row][col]
    # print('Coming from ',direction,' - ',char,'(',row,col,')')

    # Change direction depending on current pipe or break loop
    # NOTE: | and - don't change direction
    if char == '.' or char == 'S':
      break
    elif char == 'L':
      if direction == 's':
        direction = 'e'
      elif direction == 'w':
        direction = 'n'
    elif char == 'J':
      if direction == 'e':
        direction = 'n'
      elif direction == 's':
        direction = 'w'
    elif char == '7':
      if direction == 'e':
        direction = 's'
      elif direction == 'n':
        direction = 'w'
    elif char == 'F':
      if direction == 'n':
        direction = 'e'
      elif direction == 'w':
        direction = 's'
    
    c = (direction, (row+MOVES[direction][0], col+MOVES[direction][1]))
    dist += 1
  print('Answer 1 is:', int(dist/2))

# Largely the same in beginning as part one: Find loop but get all the loop nodes this time
# We count how often we've entered and left the loop so far by looking at going north pipe pieces -> if odd inside else outside
def part_two(inp: str):
  grid = []
  MOVES = {'n': (-1,0), 'e': (0,1), 's':(1,0), 'w':(0,-1)}

  # Build grid and find S
  start = ()
  for i,line in enumerate(inp.splitlines()):
    row = []
    for j,c in enumerate(list(line)):
      if c == 'S':
        start = (i,j)
      row.append(c)
    grid.append(row)

  valid_chars_for_direction = {'n': ['|','7','F'], 'e': ['-','J','7'], 's': ['|','L','J'], 'w': ['-','L','F'],}
  first_moves = []
  for direction,move in MOVES.items():
    path_char = grid[start[0]+move[0]][start[1]+move[1]]
    valid_move = path_char in valid_chars_for_direction[direction]
    if valid_move:
      first_moves.append((direction,(start[0]+move[0],start[1]+move[1])))
    
  loop_nodes = []
  # We're starting at one of the first moves and break when we find S again. That's why our initial distance is 1.
  c = first_moves.pop()
  loop_nodes.append(c[1])
  while True:
    row = c[1][0]
    col = c[1][1]
    direction = c[0]
    char = grid[row][col]

    # Change direction depending on current pipe or break loop
    # NOTE: | and - don't change direction
    if char == '.' or char == 'S':
      break
    elif char == 'L':
      if direction == 's':
        direction = 'e'
      elif direction == 'w':
        direction = 'n'
    elif char == 'J':
      if direction == 'e':
        direction = 'n'
      elif direction == 's':
        direction = 'w'
    elif char == '7':
      if direction == 'e':
        direction = 's'
      elif direction == 'n':
        direction = 'w'
    elif char == 'F':
      if direction == 'n':
        direction = 'e'
      elif direction == 'w':
        direction = 's'
    
    c = (direction, (row+MOVES[direction][0], col+MOVES[direction][1]))
    loop_nodes.append((row+MOVES[direction][0], col+MOVES[direction][1]))

  # Replace S with J 
  # NOTE: Could find this generally
  grid[start[0]][start[1]] = 'J'

  for i in range(len(grid)):
    norths = 0
    # Count "north"-facing loop pieces
    for j in range(len(grid[i])):
      c = grid[i][j]

      # If it's a loop node pointing north add to count
      if (i,j) in loop_nodes:
        if c == '|' or c == 'L' or c == 'J':
          norths += 1
        continue # To check next node (i,j), as loop node is neither O nor I
      
      if norths % 2 == 0:
        grid[i][j] = 'O'
      else:
        grid[i][j] = 'I'
  
  ans = sum([line.count("I") for line in grid])
    
  print('Answer 2 is:', ans)

# This solution expands every tile into a 3x3 representation of 
# E.g. I -> .#.
#           .#.
#           .#.
# This way loop actually has containing areas of non-zero size
def solve_with_flood_fill(inp: str):
  EXPAND_SYMBOL = {
    '|': '.#..#..#.',
    '-': '...###...',
    'L': '.#..##...',
    'J': '.#.##....',
    '7': '...##..#.',
    'F': '....##.#.',
    '.': '.........',
  }

  # Build grid and find S
  grid = []
  start = ()
  for i,line in enumerate(inp.splitlines()):
    row = []
    for j,c in enumerate(list(line)):
      if c == 'S':
        start = (i,j)
      row.append(c)
    grid.append(row)  

  # Manually replace S with correct connector pipe for input
  # NOTE: Could find this generally
  grid[start[0]][start[1]] = 'J'

  G = [["" for _ in range(len(grid[0]) * 3)] for _ in range(len(grid) * 3)]
  for r in range(len(grid)):
    for c in range(len(grid[i])):
      char = grid[r][c]
      for dr in range(3):
        for dc in range(3):
          G[r*3+dr][c*3+dc] = EXPAND_SYMBOL[char][dr * 3 + dc]

  # Use the expanded grid to find the loop
  r, c = start[0] * 3 + 1, start[1] * 3 + 1
  
  Q = deque()
  Q.append((r, c))
  seen = set()

  while Q:
    r, c = Q.popleft()
    # Check n, e, s, w
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < len(G) and 0 <= cc < len(G[0]) and (rr, cc) not in seen and G[rr][cc] == "#":
            Q.append((rr, cc))
            seen.add((rr, cc))

  print("Solution part 1:", len(seen) // 3 // 2)

  # Part 2 - Remove every pipe piece not on loop
  for r in range(len(G)):
    for c in range(len(G[0])):
        if (r, c) not in seen:
            G[r][c] = "."

  Q = deque()
  Q.append((0, 0))
  seen = set()

  while Q:
      r, c = Q.popleft()
      G[r][c] = ' ' # Outside loop points

      for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
          rr, cc = r + dr, c + dc
          if 0 <= rr < len(G) and 0 <= cc < len(G[0]) and (rr, cc) not in seen and G[rr][cc] == ".":
              Q.append((rr, cc))
              seen.add((rr, cc))
  
  # Visual of graph
  for row in G:
    print(''.join(row))

  p2 = 0
  for r in range(len(grid)):
      for c in range(len(grid[r])):
          p2 += 1 if all(G[r * 3 + dr][c * 3 + dc] == "." for dr in range(3) for dc in range(3)) else 0
  
  print("Solution part 2:", p2)

# Input
i = open('./input.txt').read().strip()
e1 = open('./example1.txt').read().strip()
e2 = open('./example2.txt').read().strip()
e3 = open('./example3.txt').read().strip()
e4 = open('./example4.txt').read().strip()


part_one(i)
solve_with_flood_fill(i)