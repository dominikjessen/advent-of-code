def build_range_bound_from_section(line: str) -> {}:
  m = []

  mappings = [x for x in line.splitlines()[1:]]

  for mapping in mappings:
    [a,b,c] = mapping.split()
    bounds = {
      'fromLowerBound': int(b),
      'fromUpperBound': int(b)+int(c)-1,
      'toLowerBound': int(a),
      'toUpperBound': int(a)+int(c)-1
    }
    m.append(bounds)

  return m

def convert(value: int, bounds: {}) -> str:
  for bound in bounds:
    if bound['fromLowerBound'] <= value <= bound['fromUpperBound']:
      offset = bound['toLowerBound']-bound['fromLowerBound']
      return str(value+offset)

  return str(value)

def convert_reverse(value: int, bounds: {}) -> str:
  for bound in bounds:
    if bound['toLowerBound'] <= value <= bound['toUpperBound']:
      offset = bound['fromLowerBound']-bound['toLowerBound']
      return str(value+offset)
    
  return str(value)

def make_seed_ranges(s: []) -> []:
  seedRanges = []
  start = 0
  length = 1

  while length < len(s):
    from_to = {'from': int(s[start]), 'to': int(s[start])+int(s[length])}
    seedRanges.append(from_to)
    start += 2
    length += 2
  
  return seedRanges

def part_one(inp: str):
  sections = inp.split('\n\n')
  seeds = sections[0].split(': ')[1].split()

  # Build range bound maps: [seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location]
  maps = [build_range_bound_from_section(sections[1]),build_range_bound_from_section(sections[2]),build_range_bound_from_section(sections[3]),build_range_bound_from_section(sections[4]),build_range_bound_from_section(sections[5]),build_range_bound_from_section(sections[6]),build_range_bound_from_section(sections[7])]

  locations = []
  for s in seeds:
    mapped = int(s)
    for m in maps:
      mapped = int(convert(mapped,m))
    locations.append(mapped)

  print('Min location 1 is:', min(locations))

# This is a reverse location -> seed, check if valid seed solution
def part_two(inp: str):
  sections = inp.split('\n\n')
  seeds = sections[0].split(': ')[1].split()
  seedRanges = make_seed_ranges(seeds)

  # Build range bound maps: [seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location]
  maps = [build_range_bound_from_section(sections[1]),build_range_bound_from_section(sections[2]),build_range_bound_from_section(sections[3]),build_range_bound_from_section(sections[4]),build_range_bound_from_section(sections[5]),build_range_bound_from_section(sections[6]),build_range_bound_from_section(sections[7])]

  # Manually parallelize by adjusting range bounds
  for l in range(0, 1):
    mapped = l
    stepsLeft = len(maps)-1
    while stepsLeft >= 0:
      mapped = int(convert_reverse(mapped, maps[stepsLeft]))
      stepsLeft -= 1
    
    # print('checking location ' + str(l) + ' with seed ' + str(mapped))
    for sr in seedRanges:
      # Edge case that first run has min seed
      if sr['from'] <= mapped <= sr['to']:
        print('mapped seed is in seeds: ', mapped)
        print('Min location 2 is: ', l)
        return


# Input
example = open('./example.txt').read().strip()
inp = open('./input.txt').read().strip()

part_one(inp)
part_two(inp)