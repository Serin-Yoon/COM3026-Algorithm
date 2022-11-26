import random

def quickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n // 2]
    small, equal, big = [], [], []
    for num in arr:
        if num < pivot:
            small.append(num)
        elif num > pivot:
            big.append(num)
        else:
            equal.append(num)
    return [small + equal + big, pivot]

def selectionProblem(arr, findIdx):
    res = quickSort(arr)
    if len(res) <= 1:
        return res[0]
    else:
        sorted, pivot = res
    pivotIdx = sorted.index(pivot)
    if findIdx == pivotIdx:
        return arr[findIdx]
    elif findIdx < pivotIdx:
        return selectionProblem(sorted[:pivotIdx], findIdx)
    else:
        findIdx -= (pivotIdx + 1)
        return selectionProblem(sorted[pivotIdx + 1:], findIdx)

arr = [random.randint(0, 1000) for i in range(500)]
findIdx = random.randint(0, 499)
pivot = 0

print("kth smallest number:", selectionProblem(arr, findIdx))