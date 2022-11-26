from tkinter import *
import tkinter.font as tkFont

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None

    # Root - Left - Right
    def preorder(self, n, result):
        if n != None:
            result.append(n.val)
            if n.left:
                self.preorder(n.left, result)
            if n.right:
                self.preorder(n.right, result)

    # Left - Root - Right
    def inorder(self, n, result):
        #print('result:', result)
        if n != None:
            if n.left:
                self.inorder(n.left, result)
            result.append(n.val)
            if n.right:
                self.inorder(n.right, result)

    # Left - Right - Root
    def postorder(self, n, result):
        if n != None:
            if n.left:
                self.postorder(n.left, result)
            if n.right:
                self.postorder(n.right, result)
            result.append(n.val)


tree = BinaryTree()
n01 = Node(60)
n02 = Node(41)
n03 = Node(74)
n04 = Node(16)
n05 = Node(53)
n06 = Node(65)
n07 = Node(25)
n08 = Node(46)
n09 = Node(55)
n10 = Node(63)
n11 = Node(70)
n12 = Node(42)
n13 = Node(62)
n14 = Node(64)

tree.root = n01
n01.left = n02
n01.right = n03
n02.left = n04
n02.right = n05
n03.left = n06
n04.right = n07
n05.left = n08
n05.right = n09
n06.left = n10
n06.right = n11
n08.left = n12
n10.left = n13
n10.right = n14

preArr = []
inArr = []
postArr = []

# Binary Tree Traversal
tree.preorder(tree.root, preArr)
tree.inorder(tree.root, inArr)
tree.postorder(tree.root, postArr)

# GUI
root = Tk()
root.title("Divde and Conquer - Binary Tree Traversal")
w = 600
h = 260
x = (root.winfo_screenwidth() - w) / 2
y = (root.winfo_screenheight() - h) / 2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
style = tkFont.Font(family="Arial", size=20, weight="bold")
style2 = tkFont.Font(family="Arial", size=15, weight="bold")

title = Label(root, text="Divide and Conquer - Binary Tree Traversal", height=2)
title.configure(font=style)
title.pack()

pre = Label(root, text="Preorder", height=2)
pre.configure(font=style2)
pre.pack()
d = Label(root, text=str(preArr), height=1)
d.pack()

in_ = Label(root, text="Inorder", height=2)
in_.configure(font=style2)
in_.pack()
d = Label(root, text=str(inArr), height=1)
d.pack()

post = Label(root, text="Postorder", height=2)
post.configure(font=style2)
post.pack()
d = Label(root, text=str(postArr), height=1)
d.pack()

root.mainloop()