# 참고 코드: https://www.youtube.com/watch?v=vSbBB4MRzp4

class Node:
    def __init__(self, data, par=None):
        self.data = list([data])
        self.parent = par
        self.child = list()

    def __str__(self):
        if self.parent:
            return str(self.parent.data) + ' - ' + str(self.data)
        return str(self.data)

    def __lt__(self, node):
        return self.data[0] < node.data[0]

    def isLeaf(self):
        return len(self.child) == 0

    def add(self, new_node):
        for child in new_node.child:
            child.parent = self
        self.data.extend(new_node.data)
        self.data.sort()
        self.child.extend(new_node.child)
        if len(self.child) > 1:
            self.child.sort()
        if len(self.data) > 2:
            self.split()

    def insert(self, new_node):
        if self.isLeaf():
            self.add(new_node)

        elif new_node.data[0] > self.data[-1]:
            self.child[-1].insert(new_node)
        else:
            for i in range(0, len(self.data)):
                if new_node.data[0] < self.data[i]:
                    self.child[i].insert(new_node)
                    break

    def split(self):
        left_child = Node(self.data[0], self)
        right_child = Node(self.data[2], self)
        if self.child:
            self.child[0].parent = left_child
            self.child[1].parent = left_child
            self.child[2].parent = right_child
            self.child[3].parent = right_child
            left_child.child = [self.child[0], self.child[1]]
            right_child.child = [self.child[2], self.child[3]]

        self.child = [left_child]
        self.child.append(right_child)
        self.data = [self.data[1]]

        if self.parent:
            if self in self.parent.child:
                self.parent.child.remove(self)
            self.parent.add(self)
        else:
            left_child.parent = self
            right_child.parent = self

    def find(self, item):
        if item in self.data:
            return item
        elif self.isLeaf():
            return False
        elif item > self.data[-1]:
            return self.child[-1].find(item)
        else:
            for i in range(len(self.data)):
                if item < self.data[i]:
                    return self.child[i].find(item)

    def remove(self, item):
        pass

    def preorder(self):
        print(self)
        for child in self.child:
            child.preorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self.root.insert(Node(item))
            while self.root.parent:
                self.root = self.root.parent
        return True

    def find(self, item):
        return self.root.find(item)

    def remove(self, item):
        self.root.remove(item)

    def preorder(self):
        self.root.preorder()


tree = Tree()
data = [59, 76, 43, 94, 29, 97, 30, 77, 49, 12, 41, 69, 29, 22, 13]
for d in data:
    tree.insert(d)
tree.preorder()