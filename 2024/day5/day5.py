import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def get_middle_number(line: str, rules: Dict[str, Dict[str, List[str]]]) -> int:
  pages = line.split(',')
  parsed = []
  occ = {}

  # Make before/after dict for current printing line
  for p in pages:
    if not p in occ:
      occ[p] = {
        "is_before": [],
        "is_after": []
      }
    
    occ[p]["is_after"] = parsed.copy()
    for pp in parsed:
      occ[pp]["is_before"].append(p)

    parsed.append(p)
  
  # Validate before and after occurrence sets with rules
  for (k,v) in occ.items():
    if not set(v["is_before"]).issubset(rules[k]["is_before"]) or not set(v["is_after"]).issubset(rules[k]["is_after"]):
      return 0

  return int(pages[len(pages)//2])

def part_one(inp: str):
  r, o = inp.split('\n\n')
  rules = {}

  # Make rule set
  for line in get_input_rows(r):
    bef, aft = line.split('|')

    if not bef in rules:
      rules[bef] = {
        "is_before": [],
        "is_after": []
      }
    
    if not aft in rules:
      rules[aft] = {
        "is_before": [],
        "is_after": []
      }

    rules[bef]["is_before"].append(aft)
    rules[aft]["is_after"].append(bef)

  s = 0
  for line in get_input_rows(o):
    s += get_middle_number(line, rules)
    
  print('Answer 1 is:', s)


############
#  Part 2  #
############

def part_two(inp: str):
  print('Answer 2 is:')


#############
#  Solving  #
#############

# Input
example = open('./example.txt').read().strip()
inp = open('./input.txt').read().strip()

# Solve example

print('Example')
print(40 * '=')

part_one(example)
part_two(example)

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp)
# part_two(inp)