# Check if provided cell is a valid cell
def is_valid(matrix, x, y) -> bool:
  return False if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[x]) else True

# TODO: Could use this for part 1 two with refactor
def get_neighbors_2(matrix,x,y) -> []:
  symbols = []
  if is_valid(matrix,x-1,y-1): # tl
    symbols.append({'char': matrix[x-1][y-1], 'coords': [x-1,y-1]})
  if is_valid(matrix,x-1,y): # t
    symbols.append({'char': matrix[x-1][y], 'coords': [x-1,y]})
  if is_valid(matrix,x-1,y+1): # tr
    symbols.append({'char': matrix[x-1][y+1], 'coords': [x-1,y+1]})
  if is_valid(matrix,x,y+1): # r
    symbols.append({'char': matrix[x][y+1], 'coords': [x,y+1]})
  if is_valid(matrix,x+1,y+1): # br
    symbols.append({'char': matrix[x+1][y+1], 'coords': [x+1,y+1]})
  if is_valid(matrix,x+1,y): # b
    symbols.append({'char': matrix[x+1][y], 'coords': [x+1,y]})
  if is_valid(matrix,x+1,y-1): # bl
    symbols.append({'char': matrix[x+1][y-1], 'coords': [x+1,y-1]})
  if is_valid(matrix,x,y-1): # l
    symbols.append({'char': matrix[x][y-1], 'coords': [x,y-1]})

  return symbols

# Get list of all neighbors for given cell (x,y)
def get_neighbors(matrix, x, y) -> []:
  symbols = []
  # tl to r
  if is_valid(matrix,x-1,y-1): # tl
    symbols.append(matrix[x-1][y-1])
  if is_valid(matrix,x-1,y): # t
    symbols.append(matrix[x-1][y])
  if is_valid(matrix,x-1,y+1): # tr
    symbols.append(matrix[x-1][y+1])
  if is_valid(matrix,x,y+1): # r
    symbols.append(matrix[x][y+1])
  if is_valid(matrix,x+1,y+1): # br
    symbols.append(matrix[x+1][y+1])
  if is_valid(matrix,x+1,y): # b
    symbols.append(matrix[x+1][y])
  if is_valid(matrix,x+1,y-1): # bl
    symbols.append(matrix[x+1][y-1])
  if is_valid(matrix,x,y-1): # l
    symbols.append(matrix[x][y-1])

  return symbols

# Check all neighbors for symbol != .
def is_part_number(adjList) -> bool:
  for cell in adjList:
    if not cell.isdigit() and cell != '.':
      return True
  return False

def part_one(inp: str):
  sum1 = 0
  numCoords = []
  matrix = []

  # Build matrix and numCoords as array of objects to check
  for i, line in enumerate(inp.splitlines()):
    currChar = ''
    currCoords = []
    row = []

    for j, char in enumerate(line):
      row.append(char)
      if char.isdigit():
        currChar += char
        currCoords.append([i,j])
        if (j == len(line)-1):
          numCoords.append({'val': currChar, 'coords': currCoords})
          currChar = ''
          currCoords = []
      else:
        if (currChar != ''):
          numCoords.append({'val': currChar, 'coords': currCoords})
          currChar = ''
          currCoords = []
    matrix.append(row)

  # For each number (dict keys), check all coords (dict values) for adjacent symbol != '.'
  for k in numCoords:
    for coord in k['coords']:
      neighbors = get_neighbors(matrix,coord[0],coord[1])
      if is_part_number(neighbors):
        sum1 += int(k['val'])
        break

  print('Sum 1 is:', sum1)

# Part 2 
def part_two(inp: str):    
  sum2 = 0
  numCoords = []
  gears = []
  matrix = []

  # TODO: this could be own function to share part 1 and 2
  for i, line in enumerate(inp.splitlines()):
    currChar = ''
    currCoords = []
    row = []

    for j, char in enumerate(line):
      row.append(char)
      if char.isdigit():
        currChar += char
        currCoords.append([i,j])
        if (j == len(line)-1):
          numCoords.append({'val': currChar, 'coords': currCoords})
          currChar = ''
          currCoords = []
      else:
        if char == '*':
          gears.append([i,j])
        if (currChar != ''):
          numCoords.append({'val': currChar, 'coords': currCoords})
          currChar = ''
          currCoords = []
    matrix.append(row)

  for gear in gears:
    neighbors = get_neighbors_2(matrix,gear[0],gear[1])
    adjNumbers = []
    numCoords2 = numCoords.copy() # Make a copy to remove from per iteration

    # If digit is found, get corresponding number for that coord pair, then remove number and coords from possible list to avoid duplicates
    for i,x in enumerate(neighbors):
      if x['char'].isdigit():
        for num in numCoords2:
          if x['coords'] in num['coords']:
            adjNumbers.append(int(num['val']))
            numCoords2.remove(num) # Make sure not to add twice
            break
      
    if len(adjNumbers) == 2:
      sum2 += adjNumbers[0] * adjNumbers[1]

  print('Sum 2 is:',sum2)

# Input
inp = open('./input.txt').read()

part_one(inp)
part_two(inp)