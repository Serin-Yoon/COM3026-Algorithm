from collections import deque

def DFS(graph, start, DFSvisited, DFSlist):
    DFSlist.append(start)
    DFSvisited[start] = True
    for node in graph[start]:
        if not DFSvisited[node]:
            DFS(graph, node, DFSvisited, DFSlist)
    return DFSlist

def BFS(graph, start, BFSvisited, BFSlist):
    queue = deque([start])
    BFSvisited[start] = True
    while queue:
        n = queue.popleft()
        BFSlist.append(n)
        for node in graph[n]:
            if not BFSvisited[node]:
                queue.append(node)
                BFSvisited[node] = True
    return BFSlist

v = int(input("정점 개수: "))
s = int(input("시작 노드: "))
f = int(input("찾는 노드: "))

DFSvisited = [False] * (v + 1)
BFSvisited = [False] * (v + 1)

graph = [[] * 1] * (v + 1)

DFSlist = []
BFSlist = []

print(BFS(graph, s, BFSvisited, BFSlist))
print(DFS(graph, s, DFSvisited, DFSlist))