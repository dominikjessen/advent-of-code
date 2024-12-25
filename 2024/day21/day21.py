from functools import cache
import sys
import os
from collections import deque
from itertools import product

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def get_next_moves(r: int, c: int) -> List[Tuple[int,int,str]]:
  return [(r - 1, c, '^'), (r, c + 1, '>'), (r + 1, c, 'v'), (r, c - 1, '<')]

def get_sequences(pad: List[str | None]) -> List[str]:
  pos = {}
  # Get all pad positions
  for r in range(len(pad)):
    for c in range(len(pad[r])):
      if pad[r][c] is not None:
        pos[pad[r][c]] = (r, c)

  # We also precompute all possible ways per input pair (to determine any short start-end on our pad)
  seqs = {}
  for a in pos:
    for b in pos:
      if a == b:
        seqs[(a,b)] = ['A'] # Just press action for e.g. 8 -> 8
        continue

      # Else let's find all possible shortest sequences from point a to point b using BFS
      options = []
      Q = deque([(pos[a], '')])
      min_path = sys.maxsize
      while Q:
        (cr, cc), c_seq = Q.popleft()
        for nr, nc, nmove in get_next_moves(cr, cc):
          if nr < 0 or nc < 0 or nr >= len(pad) or nc >= len(pad[nr]): continue
          if pad[nr][nc] is None: continue
          if pad[nr][nc] == b:
            if min_path < len(c_seq) + 1: break
            min_path = len(c_seq) + 1
            options.append(c_seq + nmove + 'A')
          else:
            Q.append(((nr, nc), c_seq + nmove))
        else:
          continue
        break

      seqs[(a,b)] = options
    
  return seqs

def pad_sequence(s: str, seqs: List[str]) -> List[str]:
  inputs = [seqs[(x,y)] for x,y in zip('A' + s, s)] # NOTE: robots always start on 'A' key
  return [''.join(x) for x in product(*inputs)]

num_pad = [
  ['7', '8', '9'],
  ['4', '5', '6'],
  ['1', '2', '3'],
  [None, '0', 'A'],
]

dir_pad = [
  [None, '^', 'A'],
  ['<', 'v', '>'],
]

# Precompute keypad shortest sequences for all possible input pairs
num_seqs = get_sequences(num_pad)
dir_seqs = get_sequences(dir_pad)

def part_one(inp: str):
  s = 0
  for l in get_input_rows(inp):
    # Robot 2 -> Direct
    r1 = pad_sequence(l, num_seqs) # This is guaranteed to be all shortest options

    # Robot 2 & 3 -> Intermediate
    curr_r = r1
    for _ in range(2):
      poss_seq = []
      for seq in curr_r:
        poss_seq += pad_sequence(seq, dir_seqs) # Need to concat the lists, not append
      min_l = min(map(len, poss_seq))
      curr_r = [seq for seq in poss_seq if len(seq) == min_l] # Filter by only the shortest input sequences

    complexity = len(curr_r[0]) * int(l[:-1])
    s += complexity

  print('Answer 1 is:', s)

############
#  Part 2  #
############

def part_two(inp: str):
  dir_lengths = {k: len(v[0]) for k,v in dir_seqs.items()}

  # Compute the shortest input length from any character a to any other character b for a given depth (i.e. nth robot)
  @cache
  def input_len(a: str, b: str, depth: int = 25) -> int:
    # We directly control, so just look at the shortest length
    if depth == 1:
      return dir_lengths[(a,b)]
    
    # Else look at all pairs and recurse keeping a rolling best counter
    best = sys.maxsize
    for seq in dir_seqs[(a,b)]:
      length = 0
      for x,y in zip('A' + seq, seq):
        length += input_len(x, y, depth - 1)

      best = min(best, length)

    return best

  s = 0
  for l in get_input_rows(inp):
    r1 = pad_sequence(l, num_seqs)
    best = sys.maxsize
    for seq in r1:
      length = 0
      for x,y in zip('A' + seq, seq):
        length += input_len(x, y)
      best = min(best, length)
    
    s += best * int(l[:-1])

  print('Answer 2 is:', s)


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
part_two(example)

# Solve input

print('\nSolution')
print(40 * '=')

part_one(inp)
part_two(inp)