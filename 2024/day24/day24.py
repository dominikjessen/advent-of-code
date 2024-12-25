import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):

  value_gates = {}
  wire_gates = {}
  zeds = {}

  starts, wirings = inp.split('\n\n')
  # Get known gate values
  for l in starts.splitlines():
    g,v = l.split(': ')
    value_gates[g] = int(v)
    if g.startswith('z'):
      zeds[g] = v

  # Make the wire gates
  for conn in wirings.splitlines():
    a,op,b,_,t = conn.split(' ')

    wire_gates[t] = (a,op,b)

    if a.startswith('z'):
      zeds[a] = None

    if b.startswith('z'):
      zeds[b] = None
    
    if t.startswith('z'):
      zeds[t] = None

  # Apply operation on wire and save value for later
  def calculate_wire_value(w: str) -> int:
    if w in value_gates: 
      return value_gates[w]

    a,op,b = wire_gates[w]
    if op == 'AND':
      val = calculate_wire_value(a) & calculate_wire_value(b)
    if op == 'OR':
      val = calculate_wire_value(a) | calculate_wire_value(b)
    if op == 'XOR':
      val = calculate_wire_value(a) ^ calculate_wire_value(b)
    
    value_gates[w] = val
    return val
  
  # Calculate our target gate values
  for k,v in zeds.items():
    zeds[k] = calculate_wire_value(k)
  
  # Now order our zeds according to their bit position and turn into binary int
  zeds = dict(sorted(zeds.items(), reverse=True))
  print('Answer 1 is:', int(''.join(map(str, zeds.values())), 2))


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