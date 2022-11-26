import random

def interpolationSearch(start, end, n):
    if start >= end or start < 0 or end < 0:
        return "Cannot Find"
    if end - start <= 1:
        if arr[start] == n:
            return start
        else:
            return "Cannot Find"
    pos = start + (n - arr[start]) * (end - start) // (arr[end] - arr[start])
    if pos < start or end < pos:
        return "Cannot Find"
    if arr[pos] == n:
        return pos
    elif arr[pos] < n:
        return interpolationSearch(pos + 1, end, n)
    else:
        return interpolationSearch(start, pos, n)

arr = [random.randint(0, 100) for i in range(10)]
arr.sort()

print(arr)
n = int(input("찾을 값: "))
print(interpolationSearch(0, len(arr) - 1, n))