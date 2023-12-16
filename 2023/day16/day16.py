# DFS / BFS with (node, direction)

# Check if provided cell is a valid cell
def is_valid(matrix, x, y) -> bool:
  return False if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[x]) else True

# known_coni

def get_energized_tiles(m: list[list[str]], start: tuple[tuple[int,int],str]) -> int:
  energized = {}

  nodes: list[tuple[tuple[int,int],str]] = []
  nodes.append(start)

  seen_with_dir = []
  while len(nodes) > 0:
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

  return len(list(energized.keys()))

def part_one(inp: str):
  m = [[c for c in list(r)] for r in inp.splitlines()]
  ans = get_energized_tiles(m, ((0,0), 'r'))
  
  print('Answer 1 is:', ans)

# NOTE: Memoized implementation notes (no time for it...)
# Could technically memoize the beam configs per run to speed up
# Global map of known_beams with final energized values (i.e. eventually that configuration leads to energized level x)
# One energized method internal map of active_beams and their history (i.e. grows every step)
# At every iteration, keep track of all active beams in run and their current positions (from curr)
# When hitting a splitter, add two new beams to active_beams --> Might want to only add if valid but probably doesn't matter
# Have to match curr node to an active beam to advance the right beam
# At start of loop check if current_active_beams is in known_beams -> return if yes
# At end of function add entire history of all active_beams during this run to the known_beams map with final energized level

# Just brute force all starts in a few seconds with PyPy
def part_two(inp: str):
  m = [[c for c in list(r)] for r in inp.splitlines()]
  max_energized = 0
  starts: list[tuple[tuple[int,int],str]] = []

  for r in range(len(m)):
    starts.append(((r,0), 'r'))
    starts.append(((r,len(m)-1), 'l'))
  
  for c in range(len(m[0])):
    starts.append(((0,c), 'd'))
    starts.append(((len(m[0])-1,c), 'u'))
  
  for s in starts:
    curr_energized = get_energized_tiles(m, s)
    if curr_energized > max_energized:
      max_energized = curr_energized
  
  print('Answer 2 is:', max_energized)

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
part_two(i)