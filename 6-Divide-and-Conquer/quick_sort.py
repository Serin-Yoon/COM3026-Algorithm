import time, random
from tkinter import *
import tkinter.font as tkFont


def quickSort(arr, depth):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[-1]
    smallArr, equalArr, bigArr = [], [], []
    for num in arr:
        if num < pivot:
            smallArr.append(num)
        elif num > pivot:
            bigArr.append(num)
        else:
            equalArr.append(num)
    mergedArr = quickSort(smallArr, depth + 1) + equalArr + quickSort(bigArr, depth + 1)
    levelArr[depth - 1].append(mergedArr)
    return mergedArr


# Create random array (length: 100) & Level array
array = random.sample(range(200), 100)
levelArr = [[0 for col in range(0)] for row in range(12)]

# Quick Sort
start = time.time()
quickSort(array, 0)
time = "Running time: " + str(time.time() - start) + " sec"

# GUI (title / running time / output)
root = Tk()
root.title("Divde and Conquer - Quick Sort")
w = 1450
h = 1000
x = (root.winfo_screenwidth() - w) / 2
y = (root.winfo_screenheight() - h) / 2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
style = tkFont.Font(family="Arial", size=20, weight="bold")
style2 = tkFont.Font(family="Arial", size=15, weight="bold")

title = Label(root, text="Divide and Conquer - Quick Sort", height=2)
title.configure(font=style)
title.pack()

t = Label(root, text=time, height=1)
t.pack()

original = Label(root, text="Original", height=2)
original.configure(font=style2)
original.pack()
d = Label(root, text=str(array), wraplength=1400)
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
    d = Label(root, text=data, wraplength=1400)
    d.pack()

root.mainloop()