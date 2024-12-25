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

# Time to build some binary addition module with carry
#
#      1 0 1 1 (11)
# +    0 1 1 1 (7)
# ----------------
# C  1 1 1 1 -
# =================
#    1 0 0 1 0 (18)

# And the final answer bit is essentially a carry bit, so it'll still fail, but we will have found our solution by then
def nth_wire_str(wire_char: str, bit: int) -> str:
  return f"{wire_char}{bit:02}"

def part_two(inp: str):
  value_gates = {}
  conns = {}

  starts, wirings = inp.split('\n\n')
  for l in starts.splitlines():
    g,v = l.split(': ')
    value_gates[g] = int(v)
  
  for conn in wirings.splitlines():
    a,op,b,_,t = conn.split(' ')

    conns[t] = (a,op,b)
  
  def assert_result(w: str, n: int) -> bool:
    print('asserting result', w, n)
    a,op,b = conns[w]
    if op != 'XOR':
      return False
    
    if n == 0:
      return sorted([a,b]) == ['x00', 'y00']

    return assert_xor(a, n) and assert_carry(b, n) or assert_xor(b,n) and assert_carry(a,n)

  def assert_xor(w: str, n: int) -> bool:
    print('asserting XOR', w, n)
    a,op,b = conns[w]

    if op != 'XOR':
      return False
  
    return sorted([a,b]) == [f"{'x'}{n:02}", f"{'y'}{n:02}"]
  
  # 0th bit has no carry
  # 1st carry bit has 2 dependent bits determining it
  # All subsequent carry bits have 3 inputs (the a, b bits' nth values and the nth carry)
  def assert_carry(w: str, n: int) -> bool:
    print('asserting carry', w, n)
    a,op,b = conns[w]
    
    if n == 1:
      if op != 'AND':
        return False
      return sorted([a,b]) == ['x00', 'y00']
    
    if op != 'OR':
      return False
    
    return assert_direct_carry(a, n - 1) and assert_recarry(b, n - 1) or assert_direct_carry(b, n - 1) and assert_recarry(a, n - 1)
  
  def assert_direct_carry(w: str, n: int) -> bool:
    print('asserting direct carry', w, n)
    a,op,b = conns[w]
    
    if op != 'AND':
      return False
    
    return sorted([a,b]) == [f"{'x'}{n:02}", f"{'y'}{n:02}"]
  
  def assert_recarry(w: str, n: int) -> bool:
    print('asserting re-carry', w, n)
    a,op,b = conns[w]
    
    if op != 'AND':
      return False
    
    return assert_xor(a, n) and assert_carry(b, n) or assert_xor(b,n) and assert_carry(a,n)

  # Now we start looping through all our z-bits and manually fix the errors
  i = 0
  while True:
    if not assert_result(f"{'z'}{i:02}", i):
      break
    i += 1

  print('Wrong wiring for', f"{'z'}{i:02}")
  swaps = ['bpf', 'fdw', 'hcc', 'hqc', 'qcw', 'z05', 'z11', 'z35']
  print('Answer 2 is:', ','.join(swaps))

# Manual solution
# z05 <> bpf
# z11 <> hcc
# hqc <> qcw
# z35 <> fdw

# Explanations
# -------------------------------
# z05 wrong! Let's find the issue
# Last debug is: asserting result z05 5 ==> error must lie with the OP for a op b --> z05. Let's check the input!
# Line: qfs AND whh -> z05 ==> This can't be correct! z05 needs to be an XOR. Let's find qfs and whh
# Line: x05 XOR y05 -> qfs ==> This is the carry bit. This one seems good.
# Line: rcr OR fkc -> whh ==> This can be a valid intermediate and we know op is wrong. Let's find qfs XOR whh
# Line: qfs XOR whh -> bpf ==> qfs XOR whh MUST be z05. So let's swap bpf and z05

# z11 wrong -- skn OR spp -> z11
# skn XOR spp doesn't exist ==> Error must be downstream
# Line: cjh AND cgn -> skn ==> this seems like it could feasibly lead us to our result skipping skn and spp
# Line: x11 AND y11 -> spp ==> correct
# Line: cgn XOR cjh -> hcc ==> culprit is hcc. Let's swap hcc and z11

# z24 wrong -- gmr XOR hqc -> z24 ==> This seems feasible, so look downstream:
# Last debugs are: asserting XOR gmr 24 & asserting XOR hqc 24
# Line: wkq OR stf -> gmr ==> seems good enough, if other one is XOR
# Line: x24 AND y24 -> hqc ==> This is the issue it needs to be the XOR
# Line: y24 XOR x24 -> qcw ==> Swap qcw with hqc

# z35 wrong -- x35 AND y35 -> z35 ==> This is accidentally the intermediate bit, so let's find something by starting with x35 XOR y35
# Line: y35 XOR x35 -> khk ==> This is still fine, so check where khk is used
# Line: khk XOR tgs -> fdw ==> This can't be an XOR, needs to be AND or OR because of what khk is ==> swap fdw with z35

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

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp)
part_two(inp)