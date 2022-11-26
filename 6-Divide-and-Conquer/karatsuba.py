from tkinter import *
import tkinter.font as tkFont


def karatsuba(x, y):
    n = len(str(x))
    m = n // 2
    x1 = x // (10 ** m)
    x0 = x % (10 ** m)
    y1 = y // (10 ** m)
    y0 = y % (10 ** m)
    L = x1 * y1
    N = x0 * y0
    M = L + N - (x1 - x0) * (y1 - y0)
    return L * (10 ** n) + M * (10 ** m) + N


def confirm():
    valX = int(blankX.get())
    valY = int(blankY.get())
    res = karatsuba(int(valX), int(valY))
    result.configure(text=res)


# GUI
root = Tk()
root.title("Divde and Conquer - Karatsuba Algorithm")
w = 600
h = 250
x = (root.winfo_screenwidth() - w) / 2
y = (root.winfo_screenheight() - h) / 2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
style = tkFont.Font(family="Arial", size=20, weight="bold")
style2 = tkFont.Font(family="Arial", size=15, weight="bold")

title = Label(root, text="Divide and Conquer - Karatsuba Algorithm", height=2)
title.configure(font=style)
title.pack()

getX = Label(root, text="x 값을 입력하세요.", height=1)
getX.pack()
blankX = Entry(root, width=5)
blankX.pack()
getY = Label(root, text="y 값을 입력하세요.", height=1)
getY.pack()
blankY = Entry(root, width=5)
blankY.pack()
btn = Button(root, text="입력", command=confirm)
btn.pack()

result = Label(root, text="", height=3)
result.configure(font=style)
result.pack()

root.mainloop()