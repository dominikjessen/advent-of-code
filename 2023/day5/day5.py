def build_range_bound_from_section(line: str) -> {}:
  # Build array of range bounds for section
  # [{'fromLowerBound': second_num, 'toLowerBound': second_num+third_num, 'toLowerBound' first_num, 'toUpperBound' first_num+third_num}]
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
  
  # No mapping found, take original
  return str(value)

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
  
  print('Min location is:', min(locations))


# Input

example = open('./example.txt').read().strip()
inp = open('./input.txt').read().strip()

part_one(inp)