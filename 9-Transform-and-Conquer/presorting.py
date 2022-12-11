import random
import time

def bruteForce(arr, find):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == find:
            cnt += 1
    if cnt > 1:
        return False
    return True

def presorting(arr, find):
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] == find:
            if arr[i + 1] == find:
                return False
    return True

arr = [random.randint(0, 50000) for i in range(10000)]
find = int(input("- Uniqueness 확인하려는 수: "))

start1 = time.time()
print(bruteForce(arr, find))
print("%.9f seconds" % (time.time() - start1))

start2 = time.time()
print(presorting(arr, find))
print("%.9f seconds" % (time.time() - start2))