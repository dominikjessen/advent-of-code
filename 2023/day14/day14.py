def count_north_load_movement(m: list[list[str]]) -> int:
  s = 0
  for c in range(len(m[0])):
    r = len(m)-1
    rock_count = 0
    while r >= 0:
      if m[r][c] == 'O':
        rock_count += 1
      if m[r][c] == '#':
        while rock_count > 0:
          s += len(m[0]) - r - rock_count
          rock_count -= 1
      
      r -= 1
    
    # Add rocks carried to edge
    while rock_count > 0:
      s += len(m[0]) - r - rock_count
      rock_count -= 1

  return s

def part_one(inp: str):
  matrix = [[c for c in list(r)] for r in inp.splitlines()]

  s = 0
  for c in range(len(matrix[0])):
    r = len(matrix)-1
    rock_count = 0
    while r >= 0:
      if matrix[r][c] == 'O':
        rock_count += 1
      if matrix[r][c] == '#':
        while rock_count > 0:
          s += len(matrix[0]) - r - rock_count
          rock_count -= 1
      
      r -= 1
    
    # Add rocks carried to edge
    while rock_count > 0:
      s += len(matrix[0]) - r - rock_count
      rock_count -= 1
    
  print('Answer 1 is:',s)

# North order is col ascending, row desc
def roll_north(m: list[list[str]]) -> list[list[str]]:
  for c in range(len(m[0])):
    r = len(m)-1
    rock_count = 0
    while r >= 0:
      if m[r][c] == 'O':
        rock_count += 1
        m[r][c] = '.'
      if m[r][c] == '#':
        while rock_count > 0:
          m[r + rock_count][c] = 'O'
          rock_count -= 1
      
      r -= 1
    
    # Add rocks carried to edge
    while rock_count > 0:
      m[r + rock_count][c] = 'O'
      rock_count -= 1
  return m

# West order is row ascending, col desc
def roll_west(m: list[list[str]]) -> list[list[str]]:
  for r in range(len(m)):
    c = len(m[0])-1
    rock_count = 0
    while c >= 0:
      if m[r][c] == 'O':
        rock_count += 1
        m[r][c] = '.'
      if m[r][c] == '#':
        while rock_count > 0:
          m[r][c+rock_count] = 'O'
          rock_count -= 1
      
      c -= 1
    
    # Add rocks carried to edge
    while rock_count > 0:
      m[r][c+rock_count] = 'O'
      rock_count -= 1
  return m

# South order is col ascending, row asc
def roll_south(m: list[list[str]]) -> list[list[str]]:
  for c in range(len(m[0])):
    r = 0
    rock_count = 0
    while r < len(m):
      if m[r][c] == 'O':
        rock_count += 1
        m[r][c] = '.'
      if m[r][c] == '#':
        while rock_count > 0:
          m[r - rock_count][c] = 'O'
          rock_count -= 1
      
      r += 1
    
    # Add rocks carried to edge
    while rock_count > 0:
      m[r - rock_count][c] = 'O'
      rock_count -= 1
  return m

# East order is row ascending, col asc
def roll_east(m: list[list[str]]) -> list[list[str]]:
  for r in range(len(m)):
    c = 0
    rock_count = 0
    while c < len(m[0]):
      if m[r][c] == 'O':
        rock_count += 1
        m[r][c] = '.'
      if m[r][c] == '#':
        while rock_count > 0:
          m[r][c-rock_count] = 'O'
          rock_count -= 1
      
      c += 1
    
    # Add rocks carried to edge
    while rock_count > 0:
      m[r][c-rock_count] = 'O'
      rock_count -= 1
  return m

def count_north_load(m: list[list[str]]) -> int:
  s = 0
  for c in range(len(m[0])):
    r = len(m)-1
    while r >= 0:
      if m[r][c] == 'O':
        s += len(m[0]) - r
      
      r -= 1

  return s

def part_two(inp: str, cycles = 1000000000):
  m = [[c for c in list(r)] for r in inp.splitlines()]

  # Roll until the pattern repeats, then calculate how far off you are from end
  grids = {}
  i = 0
  while i < cycles:
    i += 1
    m = roll_north(m)
    m = roll_west(m)
    m = roll_south(m)
    m = roll_east(m)

    s = ''.join(''.join(row) for row in m) # String of grid has hash key

    # Cycle found, fast forward
    if s in grids:
      c_len = i-grids[s] # cycle length is current iteration - iteration of first occurrence of grid
      cycles_to_skip = (cycles-i)//c_len # Cycles done / cycle length => Skip this many cycles 
      i += c_len*cycles_to_skip # Skip cycle_length * cycles many iterations -> Has remainder that will be run

    grids[s] = i

  ans = count_north_load(m)
  print('Answer 2 is:',ans)
  

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
part_two(i)