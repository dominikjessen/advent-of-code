from typing import *
from heapq import heappush, heappop
from collections import defaultdict
import math

T = TypeVar('T')

#################
# Input Parsing #
#################

def get_input_rows(inp: str) -> List[str]:
  return inp.splitlines()

def get_input_grid_int(inp: str) -> List[List[int]]:
  grid = [[int(c) for c in list(r)] for r in inp.splitlines()]
  return grid

def get_input_grid_char(inp: str) -> List[List[str]]:
  grid = [[c for c in list(r)] for r in inp.splitlines()]
  return grid

#########
# Grids #
#########

def print_grid(grid: List[List[T]]) -> None:
    for row in grid:
        print(''.join(map(str, row)))

def transpose_grid(grid: List[List[T]]) -> List[List[T]]:
    return list(map(list, zip(*grid)))

def rotate_grid_clockwise(grid: List[List[T]]) -> List[List[T]]:
    return [list(row) for row in zip(*grid[::-1])]

def get_adjacent_coords(
    x: int, 
    y: int, 
    include_diagonals: bool = False
) -> List[Tuple[int, int]]:
    directions = [
        (-1, 0),  # Up
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
    ]
    
    if include_diagonals:
        directions.extend([
            (-1, 1),  # Up-Right
            (1, 1),   # Down-Right
            (1, -1),  # Down-Left
            (-1, -1)  # Up-Left
        ])
    
    return [(x + dx, y + dy) for dx, dy in directions]

def is_valid_move(grid: List[List[T]], x: int, y: int) -> bool:
  return False if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]) else True

########
# Math #
########

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

def manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

#########
# Graph #
#########

class Graph(Generic[T]):
    def __init__(self):
        self.vertices: Set[T] = set()
        self.edges: DefaultDict[T, DefaultDict[T, int]] = defaultdict(dict)
    
    def add_edge(self, node: T, neighbor: T, weight = 0) -> None:
        self.vertices.add(node)
        self.vertices.add(neighbor)
        self.edges[node][neighbor] = weight
    
    def get_neighbors(self, node: T) -> DefaultDict[T, int]:
        return self.edges.get(node)

    def get_vertices(self) -> Set[T]:
        return self.vertices
    
    def print_graph(self) -> None:
        for node, neighbors in self.edges.items():
            for neighbor, weight in neighbors.items():
                print(f"Edge from {node} to {neighbor} with weight {weight}")

def breadth_first_search(
    graph: Graph[T], 
    start: T, 
    goal: Optional[T] = None
) -> Dict[T, Optional[T]]:
    queue: List[T] = [start]
    visited: Set[T] = {start}
    parents: Dict[T, Optional[T]] = {start: None}

    while queue:
        current = queue.pop(0)
        
        if current == goal:
            break
        
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parents[neighbor] = current
    
    return parents

def depth_first_search(
    graph: Graph[T], 
    start: T, 
    goal: Optional[T] = None
) -> Dict[T, Optional[T]]:
    stack: List[T] = [start]
    visited: Set[T] = {start}
    parents: Dict[T, Optional[T]] = {start: None}

    while stack:
        current = stack.pop()
        
        if current == goal:
            break
        
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                parents[neighbor] = current
    
    return parents

def reconstruct_path(
    parents: Dict[T, Optional[T]], 
    start: T, 
    goal: T
) -> List[T]:
    path: List[T] = []
    current: Optional[T] = goal

    while current is not None:
        path.append(current)
        current = parents.get(current)
    
    return list(reversed(path))

def dijkstra(
    graph: Dict[T, Dict[T, int]], 
    start: T
) -> Tuple[Dict[T, int], Dict[T, Optional[T]]]:
    # Initialize distances and parents
    distances: Dict[T, int] = {node: math.inf for node in graph}
    distances[start] = 0
    parents: Dict[T, Optional[T]] = {node: None for node in graph}
    
    # Priority queue to store nodes to visit
    pq: List[Tuple[int, T]] = [(0, start)]
    
    while pq:
        current_distance, current_node = heappop(pq)
        
        # If we found a longer path skip
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If we've found a shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heappush(pq, (distance, neighbor))
    
    return distances, parents

# Example usage of weighted graph
def create_weighted_graph() -> Dict[str, Dict[str, int]]:
  return {
      'A': {'B': 4, 'C': 2},
      'B': {'D': 3},
      'C': {'B': 1, 'D': 5},
      'D': {}
  }