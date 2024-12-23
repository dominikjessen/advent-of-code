import sys
import os
import networkx as nx
import itertools

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.utils import *

############
#  Part 1  #
############

def part_one(inp: str):
  # Make graph
  G = nx.Graph()
  for l in inp.splitlines():
    a,b = l.split('-')
    G.add_edge(a, b)
  
  # Could check connected for each triple pair and if yes add it
  candidates = set()
  for k,nodes in G.adjacency():
    if k[0] == 't':
      for c in itertools.combinations(nodes.keys(), 2):
        if nx.is_connected(G.subgraph(c)):
          # Sort the node candidates before adding to set so we exclude duplicates with multiple t-nodes
          add = [k, c[0], c[1]]
          add.sort()
          candidates.add((add[0], add[1], add[2]))
          
  print('Answer 1 is:', len(candidates))


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

print('\nSolution')
print(40 * '=')

part_one(inp)
# part_two(inp)