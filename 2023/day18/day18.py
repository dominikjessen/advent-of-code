def shoelace(points: list[tuple[int,int]]) -> int:
  double_area = 0

  i = len(points) - 1
  while i > 0:
    j = i - 1

    a = points[i]
    b = points[j]

    double_area += a[0] * b[1] - a[1] * b[0]
    i -= 1

  return double_area / 2
      
def part_one(inp: str):
  rows = [r.split() for r in inp.splitlines()]

  DIR_MAP: dict[str,tuple[int,int]] = { 'U': (-1,0), 'R': (0,1), 'D': (1,0), 'L': (0,-1), }

  polygon_points: list[tuple[int,int]] = [(1,1)]
  perimeter = 0

  r = 0
  c = 0
  for _i,row in enumerate(rows):
    direction, l, color = row
    length = int(l)

    # Perimeter
    perimeter += length

    # Build polygon
    delta = (DIR_MAP[direction][0] * length, DIR_MAP[direction][1] * length)
    nr = delta[0] + r
    nc = delta[1] + c
    polygon_points.append((1+nr, 1+nc))
    r = nr
    c = nc

  inside_area = shoelace(polygon_points)
  total_area = inside_area + (perimeter // 2 + 1) # Pick's theorem -> perimeter points of lagoon are outside points

  print('Answer 1 is:',int(total_area))

def part_two(inp: str):
  rows = [r.split() for r in inp.splitlines()]

  DIR_ENCODING = ['R', 'D', 'L', 'U'] # This is taken from question
  DIR_MAP: dict[str,tuple[int,int]] = { 'U': (-1,0), 'R': (0,1), 'D': (1,0), 'L': (0,-1), }

  polygon_points: list[tuple[int,int]] = [(1,1)]
  perimeter = 0

  r = 0
  c = 0
  for row in rows:
    _, _, color = row

    # Turn hex into length & direction
    hex_code = color.replace('(#','').replace(')','')
    hex_l, hex_d = hex_code[:-1],hex_code[-1]

    length = int(hex_l, 16)
    direction = DIR_ENCODING[int(hex_d)]

    # Perimeter
    perimeter += length

    # Build polygon
    delta = (DIR_MAP[direction][0] * length, DIR_MAP[direction][1] * length)
    nr = delta[0] + r
    nc = delta[1] + c
    polygon_points.append((1+nr, 1+nc))
    r = nr
    c = nc

  inside_area = shoelace(polygon_points)
  total_area = inside_area + (perimeter // 2 + 1) # Pick's theorem -> perimeter points of lagoon are outside points

  print('Answer 2 is:',int(total_area))

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
part_two(i)