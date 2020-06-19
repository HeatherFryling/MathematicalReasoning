import networkx as nx
from itertools import permutations
from itertools import combinations

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the weight of a shortest Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# You can iterate through all permutations of the set {0, ..., n-1} and find a cycle of the minimum weight.


def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Iterate through all permutations of n vertices
    #for p in permutations(range(n)):
        # Write your code here.
    min = float('inf')
    for p in permutations(list(g)):
      edge_list = get_edge_list(p)
      total = 0
      for edge in edge_list:
        total += g[edge[0]][edge[1]]['weight']
      if total < min:
        min = total
    return min

def get_edge_list(permutation):
  edge_list = []
  for i in range(len(permutation) - 1):
    edge = (permutation[i], permutation[i+1])
    edge_list.append(edge)
  edge_list.append((permutation[-1],permutation[0]))
  return edge_list


nodes = ['a', 'b', 'c', 'd', 'e']
edges = combinations(nodes, 2)
w = 'weight'
g = nx.Graph()
g.add_edges_from(edges)
g['a']['b'][w] = 2
g['a']['c'][w] = 2
g['a']['d'][w] = 3
g['a']['e'][w] = 1
g['b']['c'][w] = 3
g['b']['d'][w] = 1
g['b']['e'][w] = 5
g['c']['d'][w] = 4
g['c']['e'][w] = 3
g['d']['e'][w] = 2

print(all_permutations(g))


