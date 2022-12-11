def valid(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def nQueens(x):
    global res
    if x == N:
        res += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if valid(x):
                nQueens(x + 1)

N = 8
res = 0
row = [0] * N

nQueens(0)
print(res)