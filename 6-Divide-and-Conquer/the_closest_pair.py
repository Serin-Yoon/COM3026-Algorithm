import random

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def closestPair(start, end, level):
    if start == end:
        return float('inf')

    if end - start == 1:
        return dist(points[start], points[end])

    # Divide & Conquer
    mid = (start + end) // 2
    left = closestPair(start, mid, level + 1)
    right = closestPair(mid, end, level + 1)
    minDist = min(left, right)
    print("Point [#%d ~ #%d] vs [#%d ~ #%d] => Min: %d" % (start, mid, mid + 1, end, minDist))

    candidate = []
    for i in range(start, end + 1):
        if (points[mid][0] - points[i][0]) ** 2 < minDist:
            candidate.append(points[i])
    candidate.sort(key = lambda x: x[1])
    num = len(candidate)
    for i in range(num - 1):
        for j in range(i + 1, num):
            if (candidate[i][1] - candidate[j][1]) ** 2 < minDist:
                minDist = min(minDist, dist(candidate[i], candidate[j]))
            else:
                break

    return minDist

points = []
result = []

# 랜덤 좌표 30개 생성
for i in range(30):
    x = random.randint(0, 300)
    y = random.randint(0, 200)
    points.append([x, y])

# x축 기준 정렬
points.sort()

print(closestPair(0, 29, 0))