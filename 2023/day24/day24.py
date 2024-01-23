class Hailstone:
  def __init__(self, x, y, z, vx, vy, vz):
    self.x = x
    self.y = y
    self.z = z
    self.vx = vx
    self.vy = vy
    self.vz = vz

    # Line's a, b, c
    self.a = vy
    self.b = -vx
    self.c = vy * x - vx * y

    pass

def parallel_hail_paths(h1: Hailstone, h2: Hailstone) -> bool:
  return h1.a * h2.b == h1.b * h2.a

# Solve system with 2 line equations for a and b for x, y
def linear_eq_solution(h1: Hailstone, h2: Hailstone) -> tuple[float,float]:
  x = (h1.c * h2.b - h1.b * h2.c) / (h1.a * h2.b - h1.b * h2.a)
  y = (h1.a * h2.c - h1.c * h2.a) / (h1.a * h2.b - h1.b * h2.a)
  return (x,y)

def intersection_in_future(p: tuple[float,float], h1: Hailstone, h2: Hailstone) -> bool:
  return h1.vx * (p[0] - h1.x) >= 0 and h1.vy * (p[1] - h1.y) and h2.vx * (p[0] - h2.x) >= 0 and h2.vy * (p[1] - h2.y)

# Line form: ax + by = c
def part_one(inp: str, bounds: tuple[int,int]):
  hailstones: list[Hailstone] = []
  for line in inp.splitlines():
    h = Hailstone(*map(int, line.replace('@',',').split(',')))
    hailstones.append(h)
  
  # Check path intersection pairwise
  ans = 0
  for i, h1 in enumerate(hailstones):
    for h2 in hailstones[:i]:
      # Disregard parallel paths
      if parallel_hail_paths(h1, h2):
        continue

      # Get intersection by solving linear equation system with 2 unknowns x, y
      p = linear_eq_solution(h1, h2)
      
      # Check if collision in bounds and in future
      if bounds[0] <= p[0] <= bounds[1] and bounds[0] <= p[1] <= bounds[1] and intersection_in_future(p, h1, h2):
        ans += 1

  print('Answer 1 is:', ans)
  pass

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

# part_one(e, (7,27))
part_one(i, (200000000000000, 400000000000000))