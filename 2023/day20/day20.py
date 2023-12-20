from collections import deque

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

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()
e2 = open('./example2.txt').read().strip()

part_one(i)