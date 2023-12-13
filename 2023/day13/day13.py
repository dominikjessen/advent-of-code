from copy import deepcopy
from typing import List

def find_row_reflection(matrix) -> int:
  i = 0
  j = 1

  while j < len(matrix):
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

def off_indices(a: List[str],b: list[str]) -> list[int]:
  no_match = []
  for i in range(len(a)):
    if a[i] != b[i]:
      no_match.append(i)
    if len(no_match) > 1:
      return no_match # return early
  
  return no_match

def is_valid_with_sub(cand: (int,int), matrix, subs_made) -> bool:
  x = cand[0] - 1
  y = cand[1] + 1

  while x >= 0 and y < len(matrix):
    off = off_indices(matrix[x],matrix[y])
    if len(off) > 1 or subs_made > 1:
      return False
    if len(off) == 1:
      subs_made += 1
    if len(off) == 0:
      pass
    x -= 1
    y += 1
  
  # By the end we need to have made 1 sub exactly
  return subs_made == 1

def find_off_by_one_reflections(matrix) -> int:
  i = 0
  j = 1

  reflection_candidates = []
  while j < len(matrix):
    off = off_indices(matrix[i], matrix[j])
    if len(off) == 0:
      reflection_candidates.append((i,j,matrix,0))
    elif len(off) == 1:
      # Make a subs and append a subbed matrix with sub already made to candidates
      sub_1 = deepcopy(matrix)
      sub_1[i][off[0]] = matrix[j][off[0]]
      reflection_candidates.append((i,j,sub_1,1))
    
    i += 1
    j += 1

  for cand in reflection_candidates:
    valid = is_valid_with_sub(cand, cand[2],cand[3])
    if valid:
      return cand[0]

  return -1

def part_one(inp: str):
  s = 0
  for i,m in enumerate(inp.split('\n\n')):
    matrix = [[c for c in list(r)] for r in m.splitlines()]
    row_reflection = find_row_reflection(matrix)

    # If row reflection found, add to sum. Else, transpose and retry
    if not row_reflection == -1:
      s += 100*(row_reflection + 1)
    else:
      m_t = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]
      col_reflection = find_row_reflection(m_t) # --> Transposed row is original col
      s += col_reflection + 1

  print('Answer 1 is:',s)
  
def part_two(inp: str):
  s = 0
  for i,m in enumerate(inp.split('\n\n')):
    matrix = [[c for c in list(r)] for r in m.splitlines()]
    row_reflection = find_off_by_one_reflections(matrix)

    # If row reflection found, add to sum. Else, transpose and retry
    if not row_reflection == -1:
      s += 100*(row_reflection + 1)
    else:
      pass
      m_t = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]
      col_reflection = find_off_by_one_reflections(m_t) # --> Transposed row is original col
      s += col_reflection + 1
  print('Answer 2 is:',s)

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
part_two(i)