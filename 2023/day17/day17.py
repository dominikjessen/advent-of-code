import heapq

def is_valid(matrix, x, y) -> bool:
  return False if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[x]) else True

def hot_dijkstra(grid: list[list[int]], target: tuple[int,int], max_moves_direction = 3) -> int:
  seen = set()

  # Priority queue: (Current heat, row, col, d_r, d_c, number_of_same_dir)
  pq = [(0,0,0,0,0,0)]

  while pq:
    heat, r, c, dr, dc, steps_since_last_turn = heapq.heappop(pq)

    # Return incurred heat if at target
    if (r,c) == target:
      return heat
  
    # Prevent looping
    if (r,c,dr,dc,steps_since_last_turn) in seen:
      continue

    seen.add((r,c,dr,dc,steps_since_last_turn))

    # Can still explore in same direction
    if steps_since_last_turn < max_moves_direction and (dr,dc) != (0,0):
      new_r = r + dr
      new_c = c + dc

      if is_valid(grid, new_r, new_c):
        heapq.heappush(pq, (heat + grid[new_r][new_c], new_r, new_c, dr, dc, steps_since_last_turn + 1))

    # u, r, d, l
    DR = [-1,0,1,0]
    DC = [0,1,0,-1]

    # Try going in all directions, if valid for grid AND not straight or going back, add to queue
    for i in range(4):
      new_dr = DR[i]
      new_dc = DC[i]

      # We already went straight, we shouldn't backtrack
      if (new_dr, new_dc) != (dr,dc) and (new_dr,new_dc) != (-dr,-dc):
        nr = r + new_dr
        nc = c + new_dc

        # Making turn so steps back to 1 (first movement in direction)
        if is_valid(grid, nr, nc):
          heapq.heappush(pq, (heat + grid[nr][nc], nr, nc, new_dr, new_dc, 1))
  
  return -1

def part_one(inp: str):
  grid = [[int(c) for c in list(r)] for r in inp.splitlines()]
  target = (len(grid)-1,len(grid[0])-1)

  print('Answer 1 is:', hot_dijkstra(grid, target, 3))

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)