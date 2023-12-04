def part_one(inp: str):
  # Get points per card and immediately sum
  s = 0
  for line in inp.splitlines():
    nums = line.split(': ')[1].split()
    seen = {}
    cardPts = 0
    for num in nums:
      if num in seen:
        if cardPts == 0:
          cardPts = 1
        else:
          cardPts *= 2
      else:
        seen[num] = True
    s += cardPts

  print('Sum 1 is:', s)

def part_two(inp: str):
  # Get number of wins per card this time
  wins = []
  for line in inp.splitlines():
    nums = line.split(': ')[1].split()
    seen = {}
    cardWins = 0
    for num in nums:
      if num in seen:
        cardWins += 1
      else:
        seen[num] = True
    wins.append(cardWins)
  
  # Start with 1 copy per card
  copies = [1] * len(wins)

  # Per copy of a card, add that many copies to the next len(wins) cards
  for i in range(len(copies)):
    for j in range(wins[i]):
      copies[i+1+j] += copies[i]

  # Get sum of all copies
  s = 0
  for n in copies:
    s += n
  print ('Sum 2 is:',s)

# Input
inp = open('./input.txt').read()

part_one(inp)
part_two(inp)