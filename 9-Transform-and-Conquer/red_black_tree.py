class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = "Red"

class RB:
    def __init__(self):
        self.root = None
        self.inserted_node = None

    def find(self, data):
        return self.findNode(self.root, data)

    def findNode(self, root, data):
        if root is None or root.data == data:
            return root
        elif root.data >= data:
            return self.findNode(root.left, data)
        elif root.data < data:
            return self.findNode(root.right, data)

    def insert(self, data):
        self.root = self.insertNode(self.root, data, None)
        self.balancing(self.inserted_node)
        return

    def insertNode(self, cur, data, parent):
        if cur is None:
            cur = Node(data)
            cur.parent = parent
            self.inserted_node = cur
        else:
            if data < cur.data:
                cur.left = self.insertNode(cur.left, data, cur)
            elif data > cur.data:
                cur.right = self.insertNode(cur.right, data, cur)
        return cur

    def balancing(self, node):
        p = node.parent
        if p is None:
            node.color = "Black"
        else:
            if p.color == "Red":
                g = p.parent
                u = None
                if g.left == p:
                    u = g.right
                elif g.right == p:
                    u = g.left

                if u is not None and u.color == "Red":
                    p.color, u.color = "Black", "Black"
                    g.color = "Red"
                    self.balancing(g)
                else:
                    if p == g.left and p.left == node:
                        g.color, p.color = p.color, g.color
                        self.rightRotate(g)
                    elif p == g.left and p.right == node:
                        self.leftRotate(p)
                        g.color, node.color = node.color, g.color
                        self.rightRotate(g)
                    elif p == g.right and p.right == node:
                        g.color, p.color = p.color, g.color
                        self.leftRotate(g)
                    elif p == g.right and p.left == node:
                        self.rightRotate(p)
                        g.color, node.color = node.color, g.color
                        self.leftRotate(g)

    def leftRotate(self, node):
        c = node.right
        p = node.parent
        if c.left is not None:
            c.left.parent = node
        node.right = c.left
        node.parent = c
        c.left = node
        c.parent = p
        if p is None:
            self.root = c
        elif p is not None:
            if p.left == node:
                p.left = c
            elif p.right == node:
                p.right = c

    def rightRotate(self, node):
        c = node.left
        p = node.parent
        if c.right is not None:
            c.right.parent = node
        node.left = c.right
        node.parent = c
        c.right = node
        c.parent = p
        if p is None:
            self.root = c
        elif p is not None:
            if p.left == node:
                p.left = c
            elif p.right == node:
                p.right = c

def printTree(node):
    if node.left is not None:
        printTree(node.left)
    if node.parent != None:
        print(f'key: {node.data}, parent: {node.parent.data}, color: {node.color}')
    else:
        print(f'key: {node.data}, root: {node.parent}, color: {node.color}')
    if node.right is not None:
        printTree(node.right)


rbt = RB()
data = [1, 6, 8, 11, 13, 15, 17, 22, 25, 27]
for d in data:
    rbt.insert(d)
printTree(rbt.root)