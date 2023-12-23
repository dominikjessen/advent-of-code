import sys

def is_valid(matrix, x, y) -> bool:
  return False if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[x]) else True

seen = set()
def dfs(graph,node,end):
  if node == end:
    return 0
  
  m = -sys.maxsize

  seen.add(node)

  # For each edge out of node, try walking that path to the end
  for next_node in graph[node]:
    m = max(m, dfs(graph,next_node,end) + graph[node][next_node])

  seen.remove(node) # Remove again for next path

  return m

# NOTE: Have to contract edges leading to junctions where we have no choice of where to go for this to run efficiently
def part_one(inp: str, possible_directions):
  grid = [[c for c in list(r)] for r in inp.splitlines()]

  # Find start and end
  start = (0, grid[0].index('.'))
  end = (len(grid) - 1, grid[-1].index('.')) 

  junctions = [start,end] # Technically start end aren't junctions, but we need to include them in our graph

  # Find all path junctions
  for r,row in enumerate(grid):
    for c,char in enumerate(row):
      if char == '#':
        continue

      neighbors = 0
      DR = [-1,0,1,0]
      DC = [0,1,0,-1]
      for i in range(4):
        dr = r + DR[i]
        dc = c + DC[i]

        if is_valid(grid,dr,dc) and grid[dr][dc] != '#':
          neighbors += 1
      
      # Junction found
      if neighbors >= 3:
        junctions.append((r,c))
  
  # Build contracted graph with lengths between nodes
  graph = {node: {} for node in junctions}

  for jr, jc in junctions:
    stack = [(jr,jc,0)]
    seen = {(jr,jc)}

    while stack:
       r,c,length = stack.pop()

       if length != 0 and (r,c) in junctions:
         graph[(jr,jc)][(r,c)] = length # Add an edge from start to next junction
         continue
       
       for dr,dc in possible_directions[grid[r][c]]:
         nr = r + dr
         nc = c + dc

         if is_valid(grid,nr,nc) and grid[nr][nc] != '#' and (nr,nc) not in seen:
           stack.append((nr,nc,length+1))
           seen.add((nr,nc))

  print('Answer 1 is:', dfs(graph,start,end))
  pass

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

# Handle slopes
possible_directions = {
  '^': [(-1,0)],
  '>': [(0,1)],
  'v': [(1,0)],
  '<': [(0,-1)],
  '.': [(-1,0),(0,1),(1,0),(0,-1)]
}

part_one(i, possible_directions)