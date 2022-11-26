import time

def knapsack(limit, N, W, V):
    for r in range(N + 1):
        for c in range(limit + 1):
            if r == 0 or c == 0:
                K[r][c] = 0
            elif W[r - 1] <= c:
                K[r][c] = max(V[r - 1] + K[r - 1][c - W[r - 1]], K[r - 1][c])
            else:
                K[r][c] = K[r - 1][c]
    return K[N][limit]


limit = int(input("Weight Limit: "))
N = int(input("Item #: "))

K = [[0 for col in range(limit + 1)] for row in range(N + 1)]

W = []
V = []

for i in range(N):
    print("%d" % (i + 1), end=' ')
    w, v = map(int, input("Weight, Value: ").split())
    W.append(w)
    V.append(v)

start = time.time()
print("Maximum:", knapsack(limit, N, W, V))
print("Running time: %.9f seconds" % (time.time() - start))

