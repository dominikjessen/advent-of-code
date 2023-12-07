# Map letters to int for comparison
V = {
  'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10
}

# 5 of a kind > 4 of a kind > 3/2 > 3 of a kind > 2/2 > 2 of a kind > single high
# 7 > 6 > ... > 1
def get_handtype_value(h: str) -> int:
  cm = {}
  for c in h:
    if c in cm:
      cm[c] += 1
    else:
      cm[c] = 1
  
  # Sort value map desc
  sm = sorted(cm.items(), key=lambda x:x[1], reverse=True)

  # Map cards -> int
  for i, v in enumerate(sm):
    if v[1] == 5:
      return 7
    if v[1] == 4:
      return 6
    if v[1] == 3:
      if sm[i+1][1] == 2:
        return 5
      else:
        return 4
    if v[1] == 2:
      if sm[i+1][1] == 2:
        return 3
      else:
        return 2
    if v[1] == 1:
      return 1

def a_beats_b(a: str, b: str) -> bool:
  v_a = get_handtype_value(a)
  v_b = get_handtype_value(b)

  if v_a > v_b:
    return True
  elif v_a == v_b:
    i = 0
    for i in range(len(a)):
      c_a = V[a[i]] if a[i] in V else int(a[i])
      c_b = V[b[i]] if b[i] in V else int(b[i])
      if c_a > c_b:
        return True
      elif c_a < c_b:
        return False
  else:
    return False
  
# Basically bubble sort with weird sorting rule
def part_one(inp: str):
  hands = [{'hand': x.split()[0], 'bid': int(x.split()[1])} for x in inp.splitlines()]

  for i in range(len(hands)):
    for j in range(i+1,len(hands)):
      # If hand 1 beats hand 2, swap
      if a_beats_b(hands[i]['hand'], hands[j]['hand']):
        temp = hands[i]
        hands[i] = hands[j]
        hands[j] = temp

  s1 = 0
  for i, hand in enumerate(hands):
    s1 += (i+1)*hand['bid']

  print('Answer 1 is:', s1)


# Input
example = open('./example.txt').read().strip()
inp = open('./input.txt').read().strip()

part_one(inp)