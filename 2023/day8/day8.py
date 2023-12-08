from math import lcm

def part_one(inp: str):
  a,b = inp.split('\n\n')
  directions = a.replace('L', '0').replace('R', '1')
  nodes = {}
  for line in b.splitlines():
    split = line.split(' = ')
    nodes[split[0]] = tuple(map(str, split[1].replace('(','').replace(')','').split(', ')))
  
  steps = 0
  i = 0 # Current direction
  curr = nodes['AAA']
  while curr != nodes['ZZZ']:
    curr = nodes[curr[int(directions[i])]]
    steps += 1
    i += 1

    # Start directions over
    if i == len(directions):
      i = 0
  
  print('Answer 1 is:', steps)

# Solve using LCM (least common multiple) because input is n cycles -> every starting node hits one end node

# Each of the n starting ghosts moving along nodes (from '**A') has to constantly be moving but needs X_i steps to reach its end point
# Effectively they're moving at different speeds and you need to find when they first 'meet' at their end points '**Z'
# This is the least common multiple of each of the steps needed for ghost to reach end node
def part_two(inp: str):
  a,b = inp.split('\n\n')
  directions = a.replace('L', '0').replace('R', '1')
  nodes = {}
  for line in b.splitlines():
    split = line.split(' = ')
    nodes[split[0]] = tuple(map(str, split[1].replace('(','').replace(')','').split(', ')))
  
  starts = {k: v for k, v in nodes.items() if k[2] == 'A'}

  # Hint for cycles: each start has an end with the same neighbor nodes in reverse order
  # ends = {k: v for k, v in nodes.items() if k[2] == 'Z'}
  # print(starts)
  # print(ends)

  steps = []
  for node in starts.items():
    k,v = node

    s = 0
    i = 0
    while k[2] != 'Z':
      k = v[int(directions[i])]
      v = nodes[k]

      s += 1
      i += 1

      # Start directions over
      if i == len(directions):
        i = 0
    steps.append(s)
    
  print('Answer 2 is:', lcm(*steps))
  

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
part_two(i)