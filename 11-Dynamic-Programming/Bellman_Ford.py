def bellmanFord(v, edges, source):
    vDist = [99 for i in range(v)]
    vDist[source] = 0
    for i in range(v - 1):
        for eSource, eDest, eWeight in edges:
            if vDist[eDest] > vDist[eSource] + eWeight:
                vDist[eDest] = vDist[eSource] + eWeight
    for eSource, eDest, eWeight in edges:
        another_weight = vDist[eSource] + eWeight
        assert vDist[eDest] <= another_weight
    return vDist

edges = [
    (0, 1, 6),
    (0, 3, 7),
    (1, 2, 5),
    (1, 3, 8),
    (1, 4, -4),
    (2, 1, -2),
    (3, 2, -3),
    (3, 4, 9),
    (4, 0, 2),
    (4, 2, 7)
]

res = bellmanFord(5, edges, 0)
print(res)