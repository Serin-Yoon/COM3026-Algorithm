import random, time

def bubbleSort(arr):
    for j in range(999):
        for i in range(999):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

numArr = []

for i in range(1000):
    numArr.append(random.randrange(1, 1000))

print("Not sorted:", numArr)

start = time.time()
sortedArr = bubbleSort(numArr)
print("Sorted:", sortedArr)
print("Running time: %.9f seconds" % (time.time() - start))