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

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)
# part_two(i)