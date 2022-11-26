import random

def weight(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

# Fake Coin 1 / Constant Factor 3
def fakeCoinOne(g1, g2, g3, cnt):
    if len(g1) == 0 or len(g2) == 0 or len(g3) == 0:
        print("Fake Coin 1 Count:", cnt)
        return
    w1 = weight(g1)
    w2 = weight(g2)
    if w1 == w2:
        d = len(g3) // 3
        fakeCoinOne(g3[:d], g3[d:2*d], g3[2*d:], cnt + 1)
    elif w1 > w2:
        d = len(g2) // 3
        fakeCoinOne(g2[:d], g2[d:2*d], g2[2*d:], cnt + 1)
    else:
        d = len(g1) // 3
        fakeCoinOne(g1[:d], g1[d:2*d], g1[2*d:], cnt + 1)
    return

# Fake Coin 2 / Constant Factor
def fakeCoinTwo(g1, g2, g3, cnt):
    w1 = weight(g1)
    w2 = weight(g2)
    w3 = weight(g3)
    d1 = len(g1) // 3
    d2 = len(g2) // 3
    d3 = len(g3) // 3
    if len(g3) > len(g2):
        g3 = g3[:-1]
    if w1 == w2 and w1 < w3:
        cnt += fakeCoinTwo(g1[:d1], g1[d1:2*d1], g1[2*d1:], cnt + 1)
        cnt += fakeCoinTwo(g2[:d2], g2[d2:2*d2], g2[2*d2:], cnt + 1)
    if w1 == w2 and w2 < w3:
        cnt += fakeCoinTwo(g2[:d2], g2[d2:2*d2], g2[2*d2:], cnt + 1)
    if w1 == w2 and w1 > w3:
        cnt += fakeCoinTwo(g3[:d3], g3[d3:2*d3], g3[2*d3:], cnt + 1)
    if w1 < w2 and w1 < w3:
        cnt += fakeCoinTwo(g1[:d1], g1[d1:2*d1], g1[2*d1:], cnt + 1)
    if w1 < w2 and w1 == w3:
        cnt += fakeCoinTwo(g1[:d1], g1[d1:2*d1], g1[2*d1:], cnt + 1)
        cnt += fakeCoinTwo(g3[:d3], g3[d3:2*d3], g3[2*d3:], cnt + 1)
    if w2 < w1 and w2 < w3:
        cnt += fakeCoinTwo(g2[:d2], g2[d2:2*d2], g2[2*d2:], cnt + 1)
    if w2 < w1 and w2 == w3:
        cnt += fakeCoinTwo(g2[:d2], g2[d2:2*d2], g2[2*d2:], cnt + 1)
        cnt += fakeCoinTwo(g3[:d3], g3[d3:2*d3], g3[2*d3:], cnt + 1)
    return cnt

# Fake Coin 1
coins = [1] * 300
fakeIdx = random.randint(0, 299)
coins[fakeIdx] = 0
d = len(coins) // 3
fakeCoinOne(coins[:d], coins[d:2*d], coins[2*d:], 0)

# Fake Coin 2
coins = [1] * 300
fakeIdx1 = random.randint(0, 150)
fakeIdx2 = random.randint(150, 299)

coins[fakeIdx1] = 0
coins[fakeIdx2] = 0
d = len(coins) // 3
res = fakeCoinTwo(coins[:d], coins[d:2*d], coins[2*d:], 0)
print("Fake Coin 2 Count:", res)