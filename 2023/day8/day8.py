
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
  

# Input
i = open('./input.txt').read().strip()

part_one(i)