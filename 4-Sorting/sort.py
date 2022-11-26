### 정렬 알고리즘 3개 구현 후 실행 시간 비교

import time

# 1) 버블 정렬
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr


# 2) 삽입 정렬
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[i] < arr[j]:
                tmp = arr[i]
                del arr[i]
                arr.insert(j, tmp)
    return arr


# 3) 퀵 정렬
def quickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n // 2]
    smallArr, equalArr, bigArr = [], [], []
    for num in arr:
        if num < pivot:
            smallArr.append(num)
        elif num > pivot:
            bigArr.append(num)
        else:
            equalArr.append(num)
    return quickSort(smallArr) + equalArr + quickSort(bigArr)


arr = [3, 44, 38, 5, 47, 15, 36, 26]

start1 = time.time()
print('Bubble Sort:', bubbleSort(arr), end=' : ')
print("%.9f seconds" % (time.time() - start1))

start2 = time.time()
print('Insertion Sort:', insertionSort(arr), end=' : ')
print("%.9f seconds" % (time.time() - start2))

start3 = time.time()
print('Quick Sort:', quickSort(arr), end=' : ')
print("%.9f seconds" % (time.time() - start3))