# Parse input string to get max balls per color per game
# For part 2, these are incidentally also the mins needed per game
def get_maxes(str: str) -> []:
  maxes = []
  games = str.split('\n')

  for game in games:
    rounds = game.split(': ')[1].split(';')
    gameMax = {'red': 0, 'green': 0, 'blue': 0}
    for round in rounds:
      colors = round.split(',')
      for color in colors:
        if (color.find('red') != -1):
          r = int(color.strip().split(' ')[0])
          if (gameMax['red'] < r):
            gameMax['red'] = r
        if (color.find('green') != -1):
          g = int(color.strip().split(' ')[0])
          if (gameMax['green'] < g):
            gameMax['green'] = g
        if (color.find('blue') != -1):
          b = int(color.strip().split(' ')[0])
          if (gameMax['blue'] < b):
            gameMax['blue'] = b
    maxes.append(gameMax)    
  return maxes

# Input
inp = open('./input.txt').read()

maxes = get_maxes(inp)
balls1 = {'red': 12, 'green':13, 'blue':14}
s1 = 0
s2 = 0

# For each game check if there are enough balls available
for i,r in enumerate(maxes):
  # Part 1
  if balls1['red'] >= r['red'] and balls1['green'] >= r['green'] and balls1['blue'] >= r['blue']:
    s1 += (i+1)

  # Part 2
  s2 += (r['red']*r['green']*r['blue'])

print('Sum 1 is:',s1)
print('Sum 2 is:',s2)