import random

def binarySearch(start, end, n):
    if end - start <= 1:
        if arr[start] == n:
            print("Index:", start)
            return
        else:
            print("Cannot Find")
            return
    middle = (start + end) // 2
    if arr[middle] == n:
        print("Index:", middle)
        return
    elif arr[middle] < n:
        binarySearch(middle + 1, end, n)
    else:
        binarySearch(start, middle - 1, n)

arr = [random.randint(0, 3000) for i in range(1000)]
arr.sort()
n = int(input("찾을 수: "))
binarySearch(0, len(arr) - 1, n)