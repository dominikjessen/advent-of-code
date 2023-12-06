def part_one(inp: str):
  [t, r] = inp.splitlines()
  times = [int(x) for x in t.split(':')[1].split()[0:]]
  records = [int(x) for x in r.split(':')[1].split()[0:]]

  ans = 1

  for i in range(len(times)):
    speed = 0
    hold_beats = []

    # For early break
    best_distance = 0
    for j in range(1, times[i]):
      speed = j
      distance = speed*(times[i]-speed)
      if distance > best_distance:
        best_distance = distance

      if distance > records[i]:
        hold_beats.append(j)
      
      # Function of distance is parabola, so can break when first distance is found that's < best and < record
      if distance < best_distance and distance <= records[i]:
        break
    
    ans *= len(hold_beats)
  
  print('Answer 1 is:', ans)

def part_two(inp: str):
  [t, r] = inp.splitlines()
  time = int(t.replace(' ', '').split(':')[1])
  record = int(r.replace(' ', '').split(':')[1])

  ans = 1
  speed = 0
  hold_beats = []

  # For early break
  best_distance = 0
  for j in range(1, time):
    speed = j
    distance = speed*(time-speed)
    if distance > best_distance:
      best_distance = distance

    if distance > record:
      hold_beats.append(j)
    
    # Function of distance is parabola, so can break when first distance is found that's < best and < record
    if distance < best_distance and distance <= record:
      break
  
  ans *= len(hold_beats)
  
  print('Answer 2 is:', ans)


# Input
example = open('./example.txt').read().strip()
inp = open('./input.txt').read().strip()

part_one(inp)
part_two(inp)