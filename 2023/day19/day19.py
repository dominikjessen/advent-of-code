from collections import deque
from copy import deepcopy

def rule_applies(rule: str, part) -> bool:
  letter,operator,value = rule[0],rule[1],rule[2:]
  if operator == '<':
    return part[letter] < int(value)
  if operator == '>':
    return part[letter] > int(value)
  if operator == '<=':
    return part[letter] <= int(value)
  if operator == '>=':
    return part[letter] >= int(value)
  if operator == '=':
    return part[letter] == int(value)

def prepare_parts(part_str: str) -> []:
  parts = []
  for line in part_str.splitlines():
    x,m,a,s = line.split(',')
    x = x[3:]
    m = m[2:]
    a = a[2:]
    s = s[2:-1]
    parts.append({'x': int(x), 'm': int(m), 'a': int(a), 's': int(s)})
  
  return parts

def prepare_workflows(workflow_str: str) -> dict[str,dict['rules': list[str], 'destionations': list[str], 'fallback': str]]:
  workflows = {}
  for line in [l for l in workflow_str.splitlines()]:
    workflow_rules = []
    workflow_destinations = []
    workflow_name,data = line.split('{')
    c = data.split(',')
    for i in range(len(c)-1):
      rule,destination = c[i].split(':')
      workflow_rules.append(rule)
      workflow_destinations.append(destination)

    workflow_fallback = c[-1][:-1]

    workflows[workflow_name] = {'rules': workflow_rules, 'destinations': workflow_destinations, 'fallback': workflow_fallback}
  
  return workflows

def part_one(inp: str):
  # Get workflows and parts
  w,p = inp.split('\n\n')
  parts = prepare_parts(p)
  workflows = prepare_workflows(w)

  accepted = []
  rejected = []
  start = 'in'

  for part in parts:
    workflow = start
    while workflow != 'A' and workflow != 'R':
      for i,rule in enumerate(workflows[workflow]['rules']):
        if rule_applies(rule, part):
          workflow = workflows[workflow]['destinations'][i]
          break

        # No rules fit
        if i == len(workflows[workflow]['rules'])-1:
          workflow = workflows[workflow]['fallback']
    if workflow == 'A':
      accepted.append(part)
    elif workflow == 'R':
      rejected.append(part)

  s = 0
  for accepted_part in accepted:
    s += sum(accepted_part.values())
 
  print('Answer 1 is:',s)

def part_two(inp: str):
  w,p = inp.split('\n\n')
  workflows = prepare_workflows(w)

  initial_part = {'x': [1,4000],'m': [1,4000],'a': [1,4000],'s': [1,4000]}
  current_part = deepcopy(initial_part)

  queue = deque()
  queue.append(('in', current_part))
  accepted_parts = []

  while queue:
    (workflow,part) = queue.popleft()

    if workflow == 'R':
      continue

    if workflow == 'A':
      accepted_parts.append(part)
      continue

    # part_before_rules = deepcopy(part)
    inverse_part = deepcopy(part)

    for i,rule in enumerate(workflows[workflow]['rules']):
      letter,operator,value = rule[0],rule[1],rule[2:]

      # Adjust lower bound
      if operator == '>':
        part[letter][0] = int(value) + 1 # NOTE: + 1 ???
        inverse_part[letter][1] = int(value)

      # Adjust upper bound
      if operator == '<':
        part[letter][1] = int(value) - 1 # NOTE: - 1 ???
        inverse_part[letter][0] = int(value)

      queue.append((workflows[workflow]['destinations'][i], part))

      # Reset partition for next rule to inverse of current rule
      part = deepcopy(inverse_part)

    queue.append((workflows[workflow]['fallback'], inverse_part))


  s2 = 0
  for acc in accepted_parts:
    x = acc['x'][1] - acc['x'][0] + 1
    m = acc['m'][1] - acc['m'][0] + 1
    a = acc['a'][1] - acc['a'][0] + 1
    s = acc['s'][1] - acc['s'][0] + 1

    combinations = x * m * a * s
    s2 += combinations
  
  print('Answer 2 is:', s2)

  pass

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

# part_one(i)
part_two(i)