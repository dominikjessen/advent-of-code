def count_valid_permutations(springs: str, criteria: tuple[int, ...], known_counts: dict[tuple[str,tuple[int,...]], int] = {}) -> int:
  # No more springs left is only valid if no more criteria to fit
  if springs == '':
    return 1 if criteria == () else 0

  # No more criteria left is only valid if no more blocks of springs left to fill -> remainder of string's ? all become . -> 1 permutation
  if criteria == ():
    return 0 if '#' in springs else 1
  
  k = (springs, criteria) # Memoize

  if k in known_counts:
    return known_counts[k]
  
  result = 0

  # Operational . springs can be ignored
  if springs[0] in '.?':
    result += count_valid_permutations(springs[1:], criteria)
  
  # Potential broken spring block found
  if springs[0] in '#?':
    springs_left = len(springs)
    # Enough springs left for criteria to fit AND no . in length AND either exactly length OR one character after block that isn't #
    if criteria[0] <= springs_left and '.' not in springs[:criteria[0]] and (springs_left == criteria[0] or springs[criteria[0]] != '#'):
      # Can place a valid block here and count remaining string (+1 space for gap between blocks)
      result += count_valid_permutations(springs[criteria[0]+1:], criteria[1:])

  known_counts[k] = result
  return result

def part_one(inp: str):
  s = 0
  for line in inp.splitlines():
    springs, c = line.split(' ')
    criteria = tuple(map(int, c.split(','))) # Immutable criteria list
    s += count_valid_permutations(springs, criteria)

  print('Answer 1 is:', s)

def part_two(inp: str, fold_factor: int = 5):
  s = 0
  for line in inp.splitlines():
    spr,c = line.split(' ')

    # Unfold
    springs = '?'.join([spr]*fold_factor)
    criteria = tuple(map(int, c.split(',') * fold_factor))

    s += count_valid_permutations(springs, criteria)

  print('Answer 2 is:', s)
  
# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
part_two(i)