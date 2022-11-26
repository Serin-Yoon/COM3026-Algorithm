import random, time


def selectionSort(arr):
    for i in range(1000):
        minIdx = i
        for j in range(i + 1, 1000):
            if numArr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return numArr


numArr = []

for i in range(1000):
    numArr.append(random.randrange(1, 1000))

print("Not sorted:", numArr)

start = time.time()
sortedArr = selectionSort(numArr)
print("Sorted:", sortedArr)
print("Running time: %.9f seconds" % (time.time() - start))
