# DFS / BFS with (node, direction)

# Check if provided cell is a valid cell
def is_valid(matrix, x, y) -> bool:
  return False if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[x]) else True

def part_one(inp: str):
  m = [[c for c in list(r)] for r in inp.splitlines()]
  energized = {}

  nodes: list[tuple[tuple[int,int],str]] = []
  nodes.append(((0,0), 'r'))
  seen_with_dir = []
  iterations = 1000
  while len(nodes) > 0: # should be len nodes
    curr = nodes.pop()

    if not is_valid(m, curr[0][0], curr[0][1]):
      continue

    energized[str(str(curr[0][0])+'-'+str(curr[0][1]))] = True

    curr_as_str =  str(str(curr[0][0])+'-'+str(curr[0][1])+'-'+curr[1])

    if curr_as_str in seen_with_dir:
      continue
    else:
      seen_with_dir.append(str(str(curr[0][0])+'-'+str(curr[0][1])+'-'+curr[1]))

    if m[curr[0][0]][curr[0][1]] == '.':
      if curr[1] == 'u':
        nodes.append(((curr[0][0]-1, curr[0][1]), curr[1]))
      elif curr[1] == 'r':
        nodes.append(((curr[0][0], curr[0][1]+1), curr[1]))
      elif curr[1] == 'd':
        nodes.append(((curr[0][0]+1, curr[0][1]), curr[1]))
      elif curr[1] == 'l':
        nodes.append(((curr[0][0], curr[0][1]-1), curr[1]))
      else:
        AssertionError
    elif m[curr[0][0]][curr[0][1]] == '|':
      if curr[1] == 'u':
        nodes.append(((curr[0][0]-1, curr[0][1]), curr[1]))
      elif curr[1] == 'd':
        nodes.append(((curr[0][0]+1, curr[0][1]), curr[1]))
      elif curr[1] == 'r' or curr[1] == 'l':
        nodes.append(((curr[0][0]-1, curr[0][1]), 'u'))
        nodes.append(((curr[0][0]+1, curr[0][1]), 'd'))
      else:
        AssertionError
    elif m[curr[0][0]][curr[0][1]] == '-':
      if curr[1] == 'r':
        nodes.append(((curr[0][0], curr[0][1]+1), curr[1]))
      elif curr[1] == 'l':
        nodes.append(((curr[0][0], curr[0][1]-1), curr[1]))
      elif curr[1] == 'u' or curr[1] == 'd':
        nodes.append(((curr[0][0], curr[0][1]-1), 'l'))
        nodes.append(((curr[0][0], curr[0][1]+1), 'r'))
      else:
        AssertionError
    elif m[curr[0][0]][curr[0][1]] == '/':
      # u -> r // r -> u // d --> l // l --> d
      if curr[1] == 'u': 
        nodes.append(((curr[0][0], curr[0][1]+1), 'r'))
      elif curr[1] == 'r':
        nodes.append(((curr[0][0]-1, curr[0][1]), 'u'))
      elif curr[1] == 'd':
        nodes.append(((curr[0][0], curr[0][1]-1), 'l'))
      elif curr[1] == 'l':
        nodes.append(((curr[0][0]+1, curr[0][1]), 'd'))
      else:
        AssertionError
    elif m[curr[0][0]][curr[0][1]] == '\\':
      # u -> l // r -> d // d --> r // l --> u
      if curr[1] == 'u': 
        nodes.append(((curr[0][0], curr[0][1]-1), 'l'))
      elif curr[1] == 'r':
        nodes.append(((curr[0][0]+1, curr[0][1]), 'd'))
      elif curr[1] == 'd':
        nodes.append(((curr[0][0], curr[0][1]+1), 'r'))
      elif curr[1] == 'l':
        nodes.append(((curr[0][0]-1, curr[0][1]), 'u'))
      else:
        AssertionError

  # for r in range(len(m)):
  #   for c in range(len(m[r])):
  #     if str(str(r)+'-'+str(c)) in energized:
  #       m[r][c] = '#'
  #     else:
  #       m[r][c] = '.'
  #   print(''.join(m[r]))
  
  print('Answer 1 is:', len(list(energized.keys())))

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
# part_two(i)