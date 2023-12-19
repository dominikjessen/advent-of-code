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

def prepare_workflows(workflow_str: str) -> {}:
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

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)