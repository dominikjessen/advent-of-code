from itertools import product
import sys
import os
from collections import deque

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

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

def get_next_moves(r: int, c: int) -> List[Tuple[int,int,str]]:
  return [(r - 1, c, '^'), (r, c + 1, '>'), (r + 1, c, 'v'), (r, c - 1, '<')]

def part_one(inp: str):

  def pad_sequence(s: str, pad: List[str | None]) -> List[str]:
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
          (r,c), curr_seq = Q.popleft()
          for nr,nc,nmove in get_next_moves(r,c):
            if not is_valid_move(pad, nr,nc):
              continue
            if pad[nr][nc] is None:
              continue
            if pad[nr][nc] == b:
              if min_path < len(curr_seq) + 1:
                break
              min_path = len(curr_seq) + 1
              options.append(curr_seq + nmove + 'A')
            else:
              Q.append(((nr, nc), curr_seq + nmove))
          # NOTE: This means the inner break breaks our outer loop as well. Yay Python, we don't need a function for this
          else:
            continue
          break

        seqs[(a,b)] = options
    
    inputs = [seqs[(a,b)] for a,b in zip('A' + s, s)] # NOTE: robots always start on 'A' key
    return [''.join(x) for x in product(*inputs)]
  
  for l in get_input_rows(inp):
    print(l, pad_sequence(l, num_pad))

  print('Answer 1 is:')


############
#  Part 2  #
############

def part_two(inp: str):
  print('Answer 2 is:')


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

# print('\nSolution')
# print(40 * '=')

# part_one(inp)
# part_two(inp)