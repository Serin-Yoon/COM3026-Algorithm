def floyd(matrix):
    dist = [[99] * 9 for i in range(9)]
    for d in matrix:
        dist[d[0] - 1][d[1] - 1] = d[2]
    for k in range(9):
        dist[k][k] = 0
        for i in range(9):
            for j in range(9):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

matrix = [
    [1, 2, 8],
    [1, 3, 3],
    [1, 6, 13],
    [2, 4, 1],
    [2, 3, 2],
    [3, 2, 3],
    [3, 5, 2],
    [3, 4, 9],
    [5, 1, 5],
    [5, 4, 6],
    [4, 5, 4],
    [4, 8, 2],
    [4, 7, 6],
    [7, 8, 4],
    [7, 5, 3],
    [8, 9, 1],
    [5, 9, 4],
    [9, 7, 5],
    [5, 6, 5],
    [6, 9, 7],
    [6, 7, 1]
]

res = floyd(matrix)
for i in res:
    print(i)