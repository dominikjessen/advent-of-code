from collections import deque
from math import lcm

def ff_receives_pulse(ff_name, ff, pulse_type: str, pulses):
  # print('<< FF',ff_name,'receives',pulse_type)
  if pulse_type == 'HIGH':
    return
  if pulse_type == 'LOW':
    if ff['is_on']:
      for o in ff['outputs']:
        pulses.append(('LOW', ff_name, o))
    else:
      for o in ff['outputs']:
        pulses.append(('HIGH', ff_name, o))
    
    ff['is_on'] = not ff['is_on']

def c_receives_pulse_from(c_name, c, ff_name, pulse_type: str, pulses):
  # print('<< C',c_name,'receives',pulse_type,'from',ff_name)
  c['last_inputs'][ff_name] = pulse_type

  pulse_type_to_send = 'HIGH'
  if all(value == 'HIGH' for value in c['last_inputs'].values()):
    pulse_type_to_send = 'LOW'

  for o in c['outputs']:
    pulses.append((pulse_type_to_send, c_name, o))

def part_one(inp: str, runs: int = 1000):
  broadcaster = {}
  ff_map = {}
  c_map = {}

  # Prep modules
  for line in inp.splitlines():
    node, o = line.split(' -> ')
    outputs = o.split(', ')

    if node == 'broadcaster':
      broadcaster = outputs
    elif node[0] == '%':
      ff_map[node[1:]] = { 'is_on': False, 'outputs': outputs }
    elif node[0] == '&':
        c_map[node[1:]] = { 'last_inputs': {}, 'outputs': outputs }
  
  # Prep all conjunction modules with last_inputs
  for ff in ff_map.items():
    for ff_o in ff[1]['outputs']:
      if ff_o in c_map:
        c_map[ff_o]['last_inputs'][ff[0]] = 'LOW'

  highs = 0
  lows = 1000 # Start at 1000 to count button pushes as "LOW"

  for i in range(runs):
    # (pulse_type, source_module, target_module)
    pulses: deque[tuple[str,str,str]] = deque()
    for init_o in broadcaster:
      pulses.append(('LOW', 'broadcaster', init_o))
      
    while pulses:
      (pulse_type, source_module, target_module) = pulses.popleft()
      # print('>> Pulse:',pulse_type,'sent from', source_module_name, 'to', target_module)

      if pulse_type == 'HIGH':
        highs += 1
      elif pulse_type == 'LOW':
        lows += 1

      if target_module in ff_map:
        ff_receives_pulse(target_module, ff_map[target_module], pulse_type, pulses)
      elif target_module in c_map:
        c_receives_pulse_from(target_module, c_map[target_module], source_module, pulse_type, pulses)

  print('Highs:',highs)
  print('Lows:',lows)
  print('Answer 1 is:',highs*lows)

def find_cycle_length(inp: str, cycle_target: str) -> int:
  cycle_target = cycle_target.lower() # Just in case
  broadcaster = {}
  ff_map = {}
  c_map = {}

  # Prep modules
  for line in inp.splitlines():
    node, o = line.split(' -> ')
    outputs = o.split(', ')

    if node == 'broadcaster':
      broadcaster = outputs
    elif node[0] == '%':
      ff_map[node[1:]] = { 'is_on': False, 'outputs': outputs }
    elif node[0] == '&':
        c_map[node[1:]] = { 'last_inputs': {}, 'outputs': outputs }
  
  # Prep all conjunction modules with last_inputs
  for ff in ff_map.items():
    for ff_o in ff[1]['outputs']:
      if ff_o in c_map:
        c_map[ff_o]['last_inputs'][ff[0]] = 'LOW'
  
  for c in c_map.items():
    for c_o in c[1]['outputs']:
      if c_o in c_map:
        c_map[c_o]['last_inputs'][c[0]] = 'LOW'

  runs = 0
  while True:
    runs += 1

    # (pulse_type, source_module, target_module)
    pulses: deque[tuple[str,str,str]] = deque()
    for init_o in broadcaster:
      pulses.append(('LOW', 'broadcaster', init_o))
      
    while pulses:
      (pulse_type, source_module, target_module) = pulses.popleft()

      # Found cycle, because 'HIGH' was sent from target_source
      if source_module == cycle_target and pulse_type == 'HIGH':
        # print('Found first node cycle in',runs,'runs')
        return runs

      if target_module in ff_map:
        ff_receives_pulse(target_module, ff_map[target_module], pulse_type, pulses)
      elif target_module in c_map:
        c_receives_pulse_from(target_module, c_map[target_module], source_module, pulse_type, pulses)

# Explanation for Part 2:

# RX has only one source module for my input, which is a conjunction
# That module itself has 4 conjunction modules as inputs
# So we find the cycle length for each of those 4 -> i.e. the first time it sends a HIGH to that intermediate conjunction module
# Then we just get the LCM of all 4 (sync'd cycles) to get our answer 
# -> To send a LOW to RX, all input nodes for intermediate need to last have sent a HIGH
def part_two(inp: str):
  a = find_cycle_length(inp, 'ct')
  b = find_cycle_length(inp, 'kp')
  c = find_cycle_length(inp, 'ks')
  d = find_cycle_length(inp, 'xc')

  print('Answer 2 is:', lcm(a,b,c,d))

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()
e2 = open('./example2.txt').read().strip()

part_one(i)
part_two(i)