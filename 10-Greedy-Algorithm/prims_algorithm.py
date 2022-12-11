from collections import defaultdict
import heapq

def prim(start, edges):
  mst = []
  adjacent_edges = defaultdict(list)
  selected_vertex = set()

  for weight, node_u, node_v in edges:
    adjacent_edges[node_u].append((weight, node_u, node_v))
    adjacent_edges[node_v].append((weight, node_v, node_u))

  selected_vertex.add(start)
  candidate_edges = adjacent_edges[start]
  heapq.heapify(candidate_edges)

  while candidate_edges:
    cur_weight, cur_u, cur_v = heapq.heappop(candidate_edges)
    if cur_v not in selected_vertex:
      selected_vertex.add(cur_v)
      mst.append((cur_weight, cur_u, cur_v))
      for edge in adjacent_edges[cur_v]:
        if edge[2] not in selected_vertex:
          heapq.heappush(candidate_edges,edge)

  return mst


edges = []
n = int(input("- Edge 수: "))
for i in range(n):
  w, a, b = input("- 가중치, 노드 1, 노드 2: ").split()
  edges.append((int(w), a, b))

print("- MST:", prim('A', edges))