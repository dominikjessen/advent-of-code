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
          # print('adding to sum:',(len(matrix[0]) - r - rock_count))
          s += len(matrix[0]) - r - rock_count
          rock_count -= 1
      
      r -= 1
    
    # print('Edge hit, rocks left:',rock_count)
    # Add rocks carried to edge
    while rock_count > 0:
      # print('adding to sum:',(len(matrix[0]) - r - rock_count))
      s += len(matrix[0]) - r - rock_count
      rock_count -= 1
    
  print('Answer 1 is:',s)

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)