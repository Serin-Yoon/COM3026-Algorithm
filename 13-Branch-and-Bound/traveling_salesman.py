import math

def TSP(matrix):
    currBound = 0
    currPath = [-1] * (N + 1)
    visited = [False] * N
    for i in range(N):
        currBound += (firstMin(matrix, i) + secondMin(matrix, i))
    currBound = math.ceil(currBound / 2)
    visited[0] = True
    currPath[0] = 0
    checkTSP(matrix, currBound, 0, 1, currPath, visited)

def checkTSP(matrix, currBound, currWeight, level, currPath, visited):
    global finalPath
    if level == N:
        if matrix[currPath[level - 1]][currPath[0]] != 0:
            curr_path = currWeight + matrix[currPath[level - 1]][currPath[0]]
            if curr_path < finalPath:
                copyResult(currPath)
                finalPath = curr_path
        return
    for i in range(N):
        if matrix[currPath[level - 1]][i] != 0 and visited[i] == False:
            tmp = currBound
            currWeight += matrix[currPath[level - 1]][i]
            if level == 1:
                currBound -= ((firstMin(matrix, currPath[level - 1]) + firstMin(matrix, i)) / 2)
            else:
                currBound -= ((secondMin(matrix, currPath[level - 1]) + firstMin(matrix, i)) / 2)
            if currBound + currWeight < finalPath:
                currPath[level] = i
                visited[i] = True
                checkTSP(matrix, currBound, currWeight, level + 1, currPath, visited)
            currWeight -= matrix[currPath[level - 1]][i]
            currBound = tmp
            visited = [False] * len(visited)
            for j in range(level):
                if currPath[j] != -1:
                    visited[currPath[j]] = True

def firstMin(matrix, i):
    min = maxSize
    for k in range(N):
        if matrix[i][k] < min and i != k:
            min = matrix[i][k]
    return min

def secondMin(matrix, i):
    first, second = maxSize, maxSize
    for j in range(N):
        if i == j:
            continue
        if matrix[i][j] <= first:
            second = first
            first = matrix[i][j]

        elif (matrix[i][j] <= second and
              matrix[i][j] != first):
            second = matrix[i][j]
    return second

def copyResult(currPath):
    path[:N + 1] = currPath[:]
    path[N] = currPath[0]


maxSize = float('inf')
matrix = [
    [0, 14, 4, 10, 20],
    [14, 0, 7, 8, 7],
    [4, 5, 0, 7, 16],
    [11, 7, 9, 0, 2],
    [18, 7, 17, 4, 0]
]
N = 5
path = [None] * (N + 1)
visited = [False] * N
finalPath = maxSize

TSP(matrix)

print("Minimum cost :", finalPath)
print("Path Taken : ", end=' ')
for i in range(N + 1):
    print(path[i], end=' ')