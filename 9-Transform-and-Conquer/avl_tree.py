class Node:
    def __init__(self, key, height, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right


class AVL:
    def __init__(self):
        self.root = None

    def height(self, n):
        if n == None:
            return 0
        return n.height

    def put(self, key):
        self.root = self.putItem(self.root, key)

    def putItem(self, n, key):
        if n == None:
            return Node(key, 1)
        if n.key > key:
            n.left = self.putItem(n.left, key)
        elif n.key < key:
            n.right = self.putItem(n.right, key)
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def balance(self, n):
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotateLeft(n.left)
            n = self.rotateRight(n)
        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotateRight(n.right)
            n = self.rotateLeft(n)
        return n

    def bf(self, n):
        return self.height(n.left) - self.height(n.right)

    def rotateRight(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotateLeft(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def delete(self, key):
        self.root = self.deleteNode(self.root, key)

    def deleteNode(self, n, key):
        if n == None:
            return None
        if n.key > key:
            n.left = self.deleteNode(n.left, key)
        elif n.key < key:
            n.right = self.deleteNode(n.right, key)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n

            # n = self.minimum(target.right)
            # n.right = self.delMin(target.right)
            # n.left = target.left

            n = self.maximum(target.left)
            n.left = self.delMax(target.left)
            n.right = target.right

        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def deleteMin(self):
        if self.root == None:
            return
        self.root = self.delMin(self.root)

    def delMin(self, n):
        if n.left == None:
            return n.right
        n.left = self.delMin(n.left)
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def deleteMax(self):
        if self.root == None:
            return
        self.root = self.delMax(self.root)

    def delMax(self, n):
        if n.right == None:
            return n.left
        n.right = self.delMax(n.right)
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def max(self):
        if self.root == None:
            return None
        return self.maximum(self.root)

    def maximum(self, n):
        if n.right == None:
            return n
        return self.maximum(n.right)

    def inorder(self, n):
        if n.left:
            self.inorder(n.left)
        print(str(n.key), end=" ")
        if n.right:
            self.inorder(n.right)


avl = AVL()
avl.put(1)
avl.put(2)
avl.put(3)
avl.put(4)
avl.put(5)
avl.put(6)
avl.put(7)
avl.put(8)
avl.put(9)
avl.put(10)
avl.put(11)
avl.put(12)
avl.delete(10)

print(avl.root.left.key)
print(avl.root.right.key)

avl.inorder(avl.root)
