def part_one(inp: str):
  grid = []
  col_galaxy_count = {}
  for i,line in enumerate(inp.splitlines()):
    row = []
    row_empty = False # If row is not empty we can append it twice
    if line.find('#') == -1:
      row_empty = True
    for j,c in enumerate(line):
      if c == '#':
        col_galaxy_count[str(j)] = 1
      elif not str(j) in col_galaxy_count:
        col_galaxy_count[str(j)] = 0
      row.append(c)
    grid.append(row)

    # Append again if row empty
    if row_empty:
      grid.append(row)

  empty_cols = [int(k) for k,v in col_galaxy_count.items() if v == 0]
  expanded_g = []
  for row in grid:
    # Offset column expansion string by index to account for previous expansions
    for i,c in enumerate(empty_cols):
      row = row[:(c+i)] + ['.'] + row[(c+i):]
    expanded_g.append(row)
  
  # NOTE: This can probably be refactored out by immediately getting galaxies in first loop and then transposing positions
  galaxies = []
  for i in range(len(expanded_g)):
    for j in range(len(expanded_g[i])):
      if expanded_g[i][j] == '#':
        galaxies.append((i,j))

  
  s = 0
  for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
      diff = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
      # print('diff between ', i+1, j+1, ' is ', diff)
      s += diff
  
  print('Answer 1 is:', s)

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
# part_two(i)