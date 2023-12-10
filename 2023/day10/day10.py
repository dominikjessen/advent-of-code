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

# Input
i = open('./input.txt').read().strip()
e1 = open('./example1.txt').read().strip()

part_one(i)