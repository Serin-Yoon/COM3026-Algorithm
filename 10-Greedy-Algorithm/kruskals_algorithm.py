alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
edges = [
    (3, 0, 1), (2, 0, 5), (17, 1, 2), (16, 1, 3), (18, 2, 8),
    (8, 2, 3), (11, 3, 4), (4, 3, 8), (10, 8 ,4), (12, 8, 7),
    (9, 8, 9), (6, 4, 6), (5, 4, 7), (13, 7, 9), (15, 7, 6),
    (1, 5, 4), (7, 5, 6),
]

n = 10
p = [0]
mst = []

for i in range(1, n + 1):
    p.append(i)

def find(a):
    if a != p[a]:
        p[a] = find(p[a])
    return p[a]

def union(a, b):
    root1 = find(a)
    root2 = find(b)
    p[root2] = root1

tree_edges = 0

while True:
    if tree_edges == n-1:
        break
    w, a, b = edges.pop(0)
    if find(a) != find(b):
        union(a, b)
        mst.append((w, alpha[a], alpha[b]))
        tree_edges += 1

print("- MST:", mst)