# Tricky part here is to remember to switch directions when curved pipe is encountered
# NOTE: Because input only has 2 possible paths from S (i.e. both sides of same loop), just walk along one until back to S. 
# NOTE: Else, would have to follow one path first until impossible move
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

# Input
i = open('./input.txt').read().strip()
e1 = open('./example1.txt').read().strip()

part_one(i)
part_two(i)