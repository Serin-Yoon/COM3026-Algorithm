from tkinter import *
import tkinter.font as tkFont


def strassen():
    A00 = int(blankA00.get())
    A01 = int(blankA01.get())
    A10 = int(blankA10.get())
    A11 = int(blankA11.get())

    B00 = int(blankB00.get())
    B01 = int(blankB01.get())
    B10 = int(blankB10.get())
    B11 = int(blankB11.get())

    M1 = (A00 + A11) * (B00 + B11)
    M2 = (A10 + A11) * B00
    M3 = A00 * (B01 - B11)
    M4 = A11 * (B10 - B00)
    M5 = (A00 + A01) * B11
    M6 = (A10 - A00) * (B00 + B01)
    M7 = (A01 - A11) * (B10 + B11)

    C00 = M1 + M4 - M5 + M7
    C01 = M3 + M5
    C10 = M2 + M4
    C11 = M1 + M3 - M2 + M6

    res = ("[%d %d, %d %d]" % (C00, C01, C10, C11))
    result.configure(text=res)


# GUI
root = Tk()
root.title("Divde and Conquer - Strassen's Matrix Multiplication")
w = 600
h = 400
x = (root.winfo_screenwidth() - w) / 2
y = (root.winfo_screenheight() - h) / 2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
style = tkFont.Font(family="Arial", size=20, weight="bold")
style2 = tkFont.Font(family="Arial", size=15, weight="bold")

title = Label(root, text="Divide and Conquer - Karatsuba Algorithm", height=2)
title.configure(font=style)
title.pack()

getA = Label(root, text="A00, A01, A10, A11 값을 입력하세요.", height=1)
getA.pack()

blankA00 = Entry(root, width=5)
blankA00.pack()

blankA01 = Entry(root, width=5)
blankA01.pack()

blankA10 = Entry(root, width=5)
blankA10.pack()

blankA11 = Entry(root, width=5)
blankA11.pack()

getB = Label(root, text="B00, B01, B10, B11 값을 입력하세요.", height=1)
getB.pack()

blankB00 = Entry(root, width=5)
blankB00.pack()

blankB01 = Entry(root, width=5)
blankB01.pack()

blankB10 = Entry(root, width=5)
blankB10.pack()

blankB11 = Entry(root, width=5)
blankB11.pack()

btn = Button(root, text="입력", command=strassen)
btn.pack()

result = Label(root, text="", height=3)
result.configure(font=style)
result.pack()

root.mainloop()