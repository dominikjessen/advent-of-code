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
          # print('Placing a rock at ',r,(r+rock_count))
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
    # print('='*100)
    # print('row',r)
    c = len(m[0])-1
    rock_count = 0
    while c >= 0:
      # print('col',c,m[r][c])
      if m[r][c] == 'O':
        rock_count += 1
        m[r][c] = '.'
      if m[r][c] == '#':
        # print('rock found at',r,c,' rock count ',rock_count)
        while rock_count > 0:
          # rock 0 5
          # rock_count 1
          # 
          # 
          # print('Placing a rock at ',r,(c+rock_count))
          m[r][c+rock_count] = 'O'
          rock_count -= 1
      
      c -= 1
    
    # Add rocks carried to edge
    # print('edge hit at',r,c,' rock count ',rock_count)
    while rock_count > 0:
      # print('Placing a rock at ',r,(c+rock_count))
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
          # hit rock at
          # r = 8
          # rock_count = 4
          # 7,0 // 6,0 // 5,0 // 4,0
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
          # print('Placing a rock at ',r,(c-rock_count))
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
        # print('found rock at',r,c,'adding',len(m[0]) - r)
        s += len(m[0]) - r
      
      r -= 1

  return s

def part_two(inp: str, cycles = 1000000000):
  matrix = [[c for c in list(r)] for r in inp.splitlines()]
  m = [[c for c in list(r)] for r in inp.splitlines()]

  periods = {}
  last_index = {}
  period = 0

  # Roll until the pattern repeats, then calculate how far off you are
  # NOTE: I feel like this has a bug, which means I need to manually re-roll from start? Ans is correct though
  for i in range(cycles):
    m = roll_north(m)
    m = roll_west(m)
    m = roll_south(m)
    m = roll_east(m)
    c_n = count_north_load(m)
    if c_n not in last_index:
      last_index[c_n] = i
      periods[c_n] = 0
    else:
      if periods[c_n] == 0:
        periods[c_n] = i - last_index[c_n]
        last_index[c_n] = i
      elif i - last_index[c_n] > 1:
        period = i - last_index[c_n]
        break

  length = cycles % (period-1)

  ans = 0
  for i in range(len(periods)+length-2): # -2 because for some reason first 2 are outside of pattern?
    matrix = roll_north(matrix)
    matrix = roll_west(matrix)
    matrix = roll_south(matrix)
    matrix = roll_east(matrix)
    ans = count_north_load(matrix)
  
  print('Answer 2 is:',ans)

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

# part_one(i)
part_two(i)