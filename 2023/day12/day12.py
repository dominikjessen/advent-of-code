from typing import List

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

def part_one(inp: str):
  springs: List[str] = []
  criteria: List[List[int]] = []
  for line in inp.splitlines():
    sp,c = line.split(' ')
    springs.append(sp)
    criteria.append([int(x) for x in c.split(',')])

  s1: int = 0
  # Generate all permutations per spring string
  for i,s in enumerate(springs):
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
      if string_fits_criteria(p, criteria[i]):
        # print('Found a fitting arrangement: ',p,criteria[i])
        # print('Original string: ',springs[i])
        arrangements += 1
    
    # print('Original string: ',str(i+1),springs[i],' Arrangements: ', str(arrangements))
    s1 += arrangements
  
  print('Answer 1 is:',s1)

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()
e_small = open('./example_small.txt').read().strip()

part_one(i)
# part_two(i)