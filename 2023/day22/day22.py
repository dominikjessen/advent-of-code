# NOTE: Problem assumes z index is horizontal!
def part_one(inp: str):
  # Helper fn to check overlapping intervals (   [  ) ] --> true, bc s2 < e1 || ( ) [] --> false
  def overlapping(one, two) -> bool:
    return max(one[0], two[0]) <= min(one[3], two[3]) and max(one[1], two[1]) <= min(one[4], two[4])

  # Turn bricks into list [x1, y1, z1, x2, y2, z2] and sort by z (i.e. height)
  bricks = [list(map(int, line.replace('~', ',').split(','))) for line in inp.splitlines()]
  bricks.sort(key=lambda brick: brick[2])

  # Move bricks all the way down starting at lowest brick
  for i, brick in enumerate(bricks):
    max_z = 1
    for dropped_brick in bricks[:i]:
      # If brick overlaps existing brick, found end drop position at its top z value + 1
      if overlapping(brick, dropped_brick):
        max_z = max(max_z, dropped_brick[5] + 1)
      
      # Adjust z positions of dropped brick starting with top first to use old start
      brick[5] -= brick[2] - max_z
      brick[2] = max_z
  
  # After dropping the bricks, sort by z again
  bricks.sort(key=lambda brick: brick[2])

  # Determine which bricks support which other bricks, and which bricks are supported by which other bricks (bidirectional maps)
  k_supports = {a: set() for a in range(len(bricks))}
  k_supported_by = {b: set() for b in range(len(bricks))}

  for upper_i, upper in enumerate(bricks):
    for lower_i, lower in enumerate(bricks[:upper_i]):
      if overlapping(lower, upper) and lower[5] + 1 == upper[2]:
        k_supports[lower_i].add(upper_i) 
        k_supported_by[upper_i].add(lower_i)

  # Count bricks that can be disintegrated
  ans = 0
  for i in range(len(bricks)):
    # Brick i only supports bricks that have other supports
    if all(len(k_supported_by[j]) >= 2 for j in k_supports[i]):
      ans += 1
  
  print('Answer 1 is:',ans)
  pass

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
# part_two(e)