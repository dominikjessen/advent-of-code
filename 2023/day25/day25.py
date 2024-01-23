import networkx as nx

def part_one(inp: str):
  G = nx.Graph()

  # Build graph
  for line in inp.splitlines():
    node, neighbors = line.split(':')
    neighbors = neighbors.strip().split(' ')
    for n in neighbors:
      G.add_edge(node, n)

  # Make minimum cut (will cut 3 edges)
  G.remove_edges_from(nx.minimum_edge_cut(G))
  
  # Product of len of connected components is answer
  a, b = nx.connected_components(G)
  print('Answer 1 is:',len(a) * len(b))
  pass

# Input
i = open('./input.txt').read().strip()
e = open('./example.txt').read().strip()

part_one(i)