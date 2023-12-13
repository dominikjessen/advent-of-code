def find_row_reflection(matrix) -> int:
  i = 0
  j = 1

  while j < len(matrix):
    # print('comparing',i,j,''.join(matrix[i]),'    ',''.join(matrix[j]), matrix[i] == matrix[j])
    # Found a candidate
    if matrix[i] == matrix[j]:
      x = i - 1
      y = j + 1
      
      while x >= 0 and y < len(matrix):
        if matrix[x] == matrix[y]:
          x -= 1
          y += 1
        else:
          break
      
      # Ran out of space on one side with no error -> row reflection found
      if x < 0 or y >= len(matrix):
        return i
    
    i += 1
    j += 1

  return -1

def part_one(inp: str):
  s = 0
  for i,m in enumerate(inp.split('\n\n')):
    matrix = [[c for c in list(r)] for r in m.splitlines()]
    row_reflection = find_row_reflection(matrix)

    # If row reflection found, add to sum. Else, transpose and retry
    if not row_reflection == -1:
      # print('Matrix',i+1,'row reflected',row_reflection)
      s += 100*(row_reflection + 1)
    else:
      m_t = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]
      col_reflection = find_row_reflection(m_t) # --> Transposed row is original col
      # print('Matrix',i+1,'col reflected',col_reflection)
      s += col_reflection + 1

  print('Answer 1 is:',s)
  

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()
e2 = open('./example2.txt').read().strip()
e3 = open('./example3.txt').read().strip()

part_one(i)