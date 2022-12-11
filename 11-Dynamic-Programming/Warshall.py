def warshall(matrix):
    m = len(matrix)
    for k in range(m):
        for i in range(m):
            for j in range(m):
                matrix[i][j] = max(matrix[i][j], matrix[i][k] and matrix[k][j])
    return matrix

matrix = [
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0]
]

res = warshall(matrix)
for i in res:
    print(i)