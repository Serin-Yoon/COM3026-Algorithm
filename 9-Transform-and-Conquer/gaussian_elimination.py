def gaussianElimination(matrix):
    m = len(matrix)
    for k in range(m):
        pivots = [abs(matrix[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k
        matrix[k], matrix[i_max] = matrix[i_max], matrix[k]
        for i in range(k + 1, m):
            f = matrix[i][k] / matrix[k][k]
            for j in range(k + 1, m + 1):
                matrix[i][j] -= matrix[k][j] * f
            matrix[i][k] = 0
    result = []
    for i in range(m - 1, -1, -1):
        result.insert(0, matrix[i][m] / matrix[i][i])
        for k in range(i - 1, -1, -1):
            matrix[k][m] -= matrix[k][i] * result[0]
    return result

matrix = [[2, -2, -4, 2, -2], [-3, 5, 8, 3, 7], [2, -1, -5, 5, 4], [1, 1, 1, 3, 2]]
print(gaussianElimination(matrix))