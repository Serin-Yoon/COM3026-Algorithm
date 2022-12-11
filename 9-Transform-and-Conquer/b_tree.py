# 참고 코드: https://github.com/rtravis/BTreePy

import bisect

class Node(object):
    def __init__(self, values=None, children=None):
        self.parent = None
        self.values = values or []
        self.children = children
        if self.children:
            for i in self.children:
                i.parent = self

    def __str__(self):
        return '%r' % (self.values)

    def printTree(self, tab=''):
        print('%s ㄴ' % tab, end=' ')
        for d in self.values:
            print(alpha[d], end=' ')
        print()
        if self.children:
            for i in self.children:
                i.printTree(tab + '  ')

    def check_valid(self, tree):
        innerNode = self.children is not None
        if innerNode:
            assert ((len(self.values) + 1) == len(self.children))
        prev = None
        for i in self.values:
            if prev is not None:
                assert (i > prev)
            prev = i

        if self.children:
            for i in self.children:
                assert (i.parent is self)
                i.check_valid(tree)

    def search(self, val):
        i = bisect.bisect_left(self.values, val)
        if (i != len(self.values) and not val < self.values[i]):
            assert (self.values[i] == val)
            return (True, self, i)

        if self.children is not None:
            assert (len(self.children) >= i and self.children[i])
            return self.children[i].search(val)
        else:
            return (False, self, i)

    def split(self, tree, val=None, slot=None, childNodes=None):
        assert (val is None or (slot is not None))

        midList = [] if val is None else [val]
        if slot is None:
            slot = 0

        splitValues = self.values[0:slot] + midList + self.values[slot:]
        medianIdx = len(splitValues) // 2

        lv = splitValues[0:medianIdx]
        medianVal = splitValues[medianIdx]
        rv = splitValues[medianIdx + 1:]

        innerNode = self.children is not None

        if innerNode:
            if childNodes is not None:
                splitChildren = (self.children[0:slot] +
                                 list(childNodes) +
                                 self.children[slot + 1:])
            else:
                splitChildren = self.children
            lc = splitChildren[0:len(lv) + 1]
            rc = splitChildren[len(lv) + 1:]
        else:
            lc = None
            rc = None

        leftNode = Node(lv, lc)
        rightNode = Node(rv, rc)

        if self.parent:
            self.parent.add(tree, medianVal, None, (leftNode, rightNode))
        else:
            newRoot = Node([medianVal], [leftNode, rightNode])
            leftNode.parent = newRoot
            rightNode.parent = newRoot
            tree.root = newRoot
            tree.height += 1
            tree.size += 1

    def add(self, tree, val, slot=None, childNodes=None):
        assert (self.children is None or childNodes)
        innerNode = self.children is not None
        if innerNode:
            assert (childNodes and len(childNodes) == 2)
        else:
            assert (childNodes is None)
            
        if slot is None:
            slot = bisect.bisect_left(self.values, val)

        if len(self.values) < tree.max_values:
            self.values.insert(slot, val)
            tree.size += 1
            if childNodes:
                for i in childNodes:
                    i.parent = self
                self.children[slot:slot + 1] = childNodes
            return True
        
        self.split(tree, val, slot, childNodes)
        return True

    def min_value(self, slot=0):
        if self.children:
            return self.children[slot].min_value()
        return self.values[0], self, 0

    def max_value(self, slot=None):
        if slot is None:
            slot = len(self.values) - 1
        if self.children:
            return self.children[slot + 1].max_value()
        return self.values[-1], self, len(self.values) - 1

    def balancing(self, tree):
        lsibling, rsibling, idx = self.get_siblings()
        assert (rsibling or lsibling or self.parent is None)
        if self.parent is None:
            return
        innerNode = self.children is not None
        if innerNode:
            assert (rsibling is None or rsibling.children is not None)
            assert (lsibling is None or lsibling.children is not None)
        else:
            assert (rsibling is None or rsibling.children is None)
            assert (lsibling is None or lsibling.children is None)
        if not innerNode:
            if rsibling and len(rsibling.values) > tree.min_values:
                sepIdx = idx
                sepVal = self.parent.values[sepIdx]
                self.parent.values[sepIdx] = rsibling.values[0]
                del rsibling.values[0]
                self.values.append(sepVal)
                return
            elif lsibling and len(lsibling.values) > tree.min_values:
                sepIdx = idx - 1
                sepVal = self.parent.values[sepIdx]
                self.parent.values[sepIdx] = lsibling.values[-1]
                del lsibling.values[-1]
                self.values.insert(0, sepVal)
                return

        if lsibling is not None:
            sepIdx = idx - 1
            ln = lsibling
            rn = self
        elif rsibling is not None:
            sepIdx = idx
            ln = self
            rn = rsibling
        else:
            assert (False)

        sepVal = self.parent.values[sepIdx]

        ln.values.append(sepVal)
        ln.values.extend(rn.values)
        del rn.values[:]
        del self.parent.values[sepIdx]
        assert (self.parent.children[sepIdx + 1] is rn)
        del self.parent.children[sepIdx + 1]
        if rn.children:
            ln.children.extend(rn.children)
            for i in rn.children:
                i.parent = ln

        if len(ln.values) > tree.max_values:
            assert (innerNode)
            ln.split(tree)

        if len(self.parent.values) < tree.min_values:
            self.parent.balancing(tree)

        if self.parent.parent is None and not self.parent.values:
            tree.root = ln
            tree.root.parent = None

    def get_siblings(self):
        if not self.parent:
            return (None, None, 0)

        assert (self.parent.children)

        lsibling = None
        rsibling = None
        idx = 0

        for i, j in enumerate(self.parent.children):
            if j is self:
                if i != 0:
                    lsibling = self.parent.children[i - 1]
                if (i + 1) < len(self.parent.children):
                    rsibling = self.parent.children[i + 1]
                idx = i
                break
        return (lsibling, rsibling, idx)


class BTree(object):
    def __init__(self, order):
        if order <= 2:
            return
        self.root = Node()
        self.order = order
        self.max_values = order - 1
        self.min_values = self.max_values // 2
        self.height = 1
        self.size = 0

    def add(self, val):
        found, node, slot = self.root.search(val)
        if found:
            return False
        return node.add(self, val, slot, None)

    def search(self, val):
        return self.root.search(val)[0]

    def min(self):
        return self.root.min_value()[0]

    def max(self):
        return self.root.max_value()[0]


tree = BTree(4)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
data = [0, 6, 5, 1, 10, 3, 7, 12, 9, 4, 18, 17, 23, 2, 11, 19, 20, 21, 14]
for d in data:
    tree.add(d)
tree.root.printTree()
