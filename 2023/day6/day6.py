from math import ceil, floor, sqrt

def get_solution(time: int, record: int) -> int:
    # Left bound
    duration_min = (time - sqrt((time**2 - 4 * record))) / 2
    ceil_duration_min = ceil(duration_min)

    # Check if bound is inclusive or not
    if duration_min == ceil_duration_min:
        x1 = int(duration_min + 1)
    else:
        x1 = ceil_duration_min

    # Right bound
    duration_max = (time + sqrt((time**2 - 4 * record))) / 2
    floor_duration_max = floor(duration_max)
    if duration_max == floor_duration_max:
        x2 = int(duration_max - 1)
    else:
        x2 = floor_duration_max

    return x2 - x1 + 1 # +1 to account for losing one way in subtraction

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

  speed = 0
  beats = 0

  # For early break
  best_distance = 0
  for j in range(1, time):
    speed = j
    distance = speed*(time-speed)
    if distance > best_distance:
      best_distance = distance

    if distance > record:
      beats += 1
    
    # Function of distance is parabola, so can break when first distance is found that's < best and < record
    if distance < best_distance and distance <= record:
      break
    
  print('Answer 2 is:', beats)

def part_one_math(inp: str):
  [t, r] = inp.splitlines()
  times = [int(x) for x in t.split(':')[1].split()[0:]]
  records = [int(x) for x in r.split(':')[1].split()[0:]]

  ans = 1

  # Distance function is a parabola -> solve for x1,x2 to get bounds of record breaking -> x2 - x1 + 1
  for i in range(len(times)):
    solutions = get_solution(times[i], records[i])
    ans *= solutions
  
  print('Answer 1 is:', ans)

def part_two_math(inp: str):
  [t, r] = inp.splitlines()
  time = int(t.replace(' ', '').split(':')[1])
  record = int(r.replace(' ', '').split(':')[1])

  ans = get_solution(time, record)
  print('Answer 2 is:', ans)


# Input
example = open('./example.txt').read().strip()
inp = open('./input.txt').read().strip()

part_one_math(inp)
part_two_math(inp)