import time, random
from tkinter import *
import tkinter.font as tkFont


def mergeSort(arr, depth):
    if len(arr) < 2:
        return arr

    # 분할
    midIdx = len(arr) // 2
    leftArr = mergeSort(arr[:midIdx], depth + 1)
    rightArr = mergeSort(arr[midIdx:], depth + 1)

    # 통합
    mergedArr = []
    i, j = 0, 0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            mergedArr.append(leftArr[i])
            i += 1
        else:
            mergedArr.append(rightArr[j])
            j += 1

    # 둘중 하나는 빈 array 이므로 순서 무관
    mergedArr += leftArr[i:]
    mergedArr += rightArr[j:]

    levelArr[depth - 1].append(mergedArr)

    return mergedArr


# Create random array (length: 50) & Level array
array = random.sample(range(100), 50)
levelArr = [[0 for col in range(0)] for row in range(6)]

# Merge Sort
start = time.time()
mergeSort(array, 0)
time = "Running time: " + str(time.time() - start) + " sec"

# GUI (title / running time / output)
root = Tk()
root.title("Divde and Conquer - Merge Sort")
w = 1250
h = 550
x = (root.winfo_screenwidth() - w) / 2
y = (root.winfo_screenheight() - h) / 2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
style = tkFont.Font(family="Arial", size=20, weight="bold")
style2 = tkFont.Font(family="Arial", size=15, weight="bold")

title = Label(root, text="Divide and Conquer - Merge Sort", height=2)
title.configure(font=style)
title.pack()

t = Label(root, text=time, height=1)
t.pack()

original = Label(root, text="Original", height=2)
original.configure(font=style2)
original.pack()
d = Label(root, text=str(array), height=1)
d.pack()

# print output
for i in range(len(levelArr)):
    text = "\nLevel " + str(i + 1)
    level = Label(root, text=text, height=2)
    level.configure(font=style2)
    level.pack()
    data = ''
    for arr in levelArr[i]:
        data += (str(arr) + ' ')
    d = Label(root, text=data, height=1)
    d.pack()

root.mainloop()