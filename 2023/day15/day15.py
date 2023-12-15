def ascii_sum(sequence: str) -> int:
  s = 0
  for c in list(sequence):
    s += ord(c)
    s = s * 17
    s = s % 256
  
  return s
  

def part_one(inp: str):
  sequences = inp.split(',')

  s = 0
  for sequence in sequences:
    s += ascii_sum(sequence)
  
  print('Answer 1 is:', s)

def part_two(inp: str):
  sequences = inp.split(',')
  boxes: list[dict[str,int]] = []

  for _i in range(256):
    boxes.append({})

  for sequence in sequences:
    if sequence.find('=') != -1:
      [label,focal_len] = sequence.split('=')
      box_idx = ascii_sum(label)
      boxes[box_idx][label] = int(focal_len)
    elif sequence.find('-') != -1:
      label = sequence[:-1]
      box_idx = ascii_sum(label)
      if label in boxes[box_idx]:
        del boxes[box_idx][label]

  s = 0
  for i,box in enumerate(boxes):
    for j,v in enumerate(box.values()):
      s += (i+1) * (j+1) * v

  print('Answer 2 is:', s)

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
part_two(i)