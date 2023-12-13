from typing import List
from functools import cache

# Turn a spring string '..##...#.###' into [2,1,3] list of broken springs of lengths
def parse_springs(springs: str) -> List[int]:
  spring_list = []
  spring_len = 0
  for i,c in enumerate(list(springs)):
    if c == '#':
      spring_len += 1
    if c == '.' and spring_len > 0:
      spring_list.append(spring_len)
      spring_len = 0 
  
  if spring_len > 0:
    spring_list.append(spring_len)

  return spring_list


def string_fits_criteria(springs: str, criteria: List[int]) -> bool:
  parsed = parse_springs(springs)
  # print('Parsed == criteria?',parsed, criteria, parsed == criteria)

  return parsed == criteria

def string_fits_criteria_tuple(springs: str, criteria: ()) -> bool:
  parsed = tuple(parse_springs(springs))
  # print('Parsed == criteria?',parsed, criteria, parsed == criteria)

  return parsed == criteria

@ cache
def get_single_arrangement_count(springs: str, criteria: ()) -> int:
  s = ''.join(springs)
  arrangements = 0
  permutations = []

  # Create a stack of permutations to permute from
  permutation_stack = []
  permutation_stack.append(s.replace('?', '#', 1))
  permutation_stack.append(s.replace('?', '.', 1))

  # print('base',permutations)

  for prev in permutation_stack:
    # No need to permutate a string that's done
    if prev.find('?') == -1:
      permutations.append(prev)
      continue
    permutation_stack.append(prev.replace('?', '#', 1))
    permutation_stack.append(prev.replace('?', '.', 1))
    # print('after',permutations)
  
  for p in permutations:

    # print('checking string', p, criteria[i])
    if string_fits_criteria_tuple(p, criteria):
      # print('Found a fitting arrangement: ',p,criteria[i])
      # print('Original string: ',springs[i])
      arrangements += 1
    
  return arrangements

# Generates all permutations per spring string, counts valid arrangements, then returns as list
def get_all_arrangements(springs: List[str], criteria: List[List[int]]) -> List[int]:
  original_arrangements: List[int] = []
  # Generate all permutations per spring string
  for i,s in enumerate(springs):
    arr = get_single_arrangement_count(s,tuple(criteria[i]))
    
    # print('Original string: ',str(i+1),springs[i],' Arrangements: ', str(arrangements))
    original_arrangements.append(arr)
    
  return original_arrangements

def count_unknowns_at_front(s: str) -> int:
  count = 0
  for c in list(s):
    if c == '?':
      count += 1
    else:
      break
  
  return count

def count_first_unknown_group(s: str) -> int:
  count = 0
  for c in list(s):
    if c == '?':
      count += 1
    elif count == 0:
      continue
    else:
      break
  
  return count

def part_one(inp: str):
  springs: List[str] = []
  criteria: List[List[int]] = []
  for line in inp.splitlines():
    sp,c = line.split(' ')
    springs.append(tuple(sp))
    criteria.append([int(x) for x in c.split(',')])

  arrangements = get_all_arrangements(springs,criteria)
  
  for i in range(len(springs)):
    print('Original string: ',str(i+1),''.join(springs[i]),' Arrangements: ', str(arrangements[i]))
  
  print('Answer 1 is:',sum(arrangements))

def part_two(inp: str):
  springs = []
  criteria: List[List[int]] = []
  for line in inp.splitlines():
    sp,c = line.split(' ')
    print(sp,'-->','?'.join([sp]*5))
    springs.append(tuple('?'.join([sp]*5)))
    criteria.append([int(x) for x in c.split(',')]*5)
  
  # arrangements = get_all_arrangements(springs,criteria)

  # print('Answer 2 is:',sum(arrangements))

def part_two_first_group(inp: str):
  springs: List[str] = []
  criteria: List[List[int]] = []
  unknowns_at_front: List[int] = []
  for line in inp.splitlines():
    sp,c = line.split(' ')
    springs.append(sp)
    unknowns_at_front.append(count_first_unknown_group(sp))
    criteria.append([int(x) for x in c.split(',')])
  
  # Build new springs
  new_springs: List[str] = []
  print('Unknowns',unknowns_at_front)
  for i,s in enumerate(springs):
    if unknowns_at_front[i] % 2 == 0:
      new_springs.append('?' + s)
    else:
      new_springs.append(s + '?')

  original_arrangements = get_all_arrangements(springs,criteria)
  new_arrangements = get_all_arrangements(new_springs,criteria)

  s2 = 0
  for i in range(len(original_arrangements)):
    # print('For string',springs[i],' Arrangements count is: ',str(original_arrangements[i] * (new_arrangements[i]**4)))
    s2 += original_arrangements[i] * (new_arrangements[i]**4)
  
  print('Answer 2 is:', s2)

# --> Looks to be wrong for 4th & 5th string in example ???
def part_two_fill_sides(inp: str):
  springs: List[str] = []
  criteria: List[List[int]] = []
  unknown_first_last: (bool,bool) = []
  for line in inp.splitlines():
    sp,c = line.split(' ')
    springs.append(sp)
    unknown_first_last.append((sp[0] == '?', sp[-1] == '?'))
    criteria.append([int(x) for x in c.split(',')])
  
  # Build new springs
  new_springs: List[str] = []
  print('Unknowns',unknown_first_last)
  for i,s in enumerate(springs):
    # First try: (1,1) -> BOTH // (1,0) -> BACK // (0,1) -> FRONT
    if unknown_first_last[i][0] and unknown_first_last[i][1]:
      new_s = '?' + s + '?'
      new_springs.append(new_s)
    elif unknown_first_last[i][0]:
      new_springs.append(s + '?')
    elif unknown_first_last[i][1]:
      new_springs.append('?' + s)
    else:
      new_s = '?' + s + '?'
      new_springs.append(new_s)

  original_arrangements = get_all_arrangements(springs,criteria)
  new_arrangements = get_all_arrangements(new_springs,criteria)

  s2 = 0
  for i in range(len(original_arrangements)):
    print('For string',springs[i],' Arrangements count is: ',str(original_arrangements[i] * (new_arrangements[i]**4)))
    s2 += original_arrangements[i] * (new_arrangements[i]**4)
  
  print('Answer 2 is:', s2)
  
# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()
efront = open('./example_front.txt').read().strip()
eback = open('./example_back.txt').read().strip()
eboth = open('./example_both.txt').read().strip()


# part_two_first_group(i) 
print('Original')
part_one(e)
print('='*100)
# part_one(i)

# print('Front')
# part_one(efront)
# print('='*100)

print('Back')
part_one(eback)
print('='*100)

# print('Both')
# part_one(eboth)
# print('='*100)
# part_two(e)

# It seems like my random idea for Part 2 is:
# Try part_one with each string with ? at front and/or (need to figure this out) ? at back of string and same criteria
# Then new_arrangements**4 * old_arrangements --> This seems to work for example if first line gets ? only at end

# part_two(i)

# In example it goes:
# 1 --> 1
# 4 --> 16384
# 1 --> 1
# 1 --> 16
# 4 --> 2500
# 10 --> 506250

# If number of ? at front even --> add front // odd --> add back
# No clue why this works but it does?

# Base idea was wrong
# 2 more ideas: --> Either instead of add front try add both

# Maybe count first and last index [0,1,2] ?
# 0 --> add both
# 1 --> 

# Maybe 4 * BACK + 1 * normal  ??? --> For some reason this is correct for 6th string, and not for 2 and 4 and 5???