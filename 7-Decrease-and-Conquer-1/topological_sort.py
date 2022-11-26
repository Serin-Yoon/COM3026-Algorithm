from collections import deque

def topologicalSort():
    order = []
    queue = deque()
    for i in range(len(vertex)):
        if inDegree[i] == 0:
            queue.append(i)
    while queue:
        curr = queue.popleft()
        order.append(curr)
        for e in edges[curr]:
            inDegree[e] -= 1
            if inDegree[e] == 0:
                queue.append(e)
    for o in order:
        print(vertex[o], end=" ")

vertex = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
edges = [
    [1, 2],
    [4, 6],
    [5],
    [0, 1, 2, 5, 6],
    [],
    [],
    [5]
]
inDegree = [0] * len(vertex)

for edge in edges:
    for e in edge:
        inDegree[e] += 1

topologicalSort()