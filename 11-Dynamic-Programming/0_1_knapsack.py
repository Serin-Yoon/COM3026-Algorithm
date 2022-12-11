def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if (wt[n - 1] > W):
        return knapSack(W, wt, val, n - 1)
    else:
        return max(
            val[n - 1] + knapSack(
                W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1))

W = 55
val = [25, 30, 45, 30, 35]
wt = [20, 15, 30, 20, 15]
print(knapSack(W, wt, val, 5))