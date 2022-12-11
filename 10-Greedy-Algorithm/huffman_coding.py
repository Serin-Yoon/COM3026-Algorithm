class Node:
    def __init__(self, alpha, freq, left=None, right=None):
        self.alpha = alpha
        self.freq = freq
        self.left = left
        self.right = right
        self.code = ""

def huffman(dic):
    nodes = []
    for e in dic:
        nodes.append(Node(e[0], e[1]))
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left, right = nodes[0], nodes[1]
        left.code, right.code = 0, 1
        newNode = Node(left.alpha + right.alpha, left.freq + right.freq, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    printCode(nodes[0])
    return

def printCode(node, val=""):
    newVal = val + str(node.code)
    if node.left:
        printCode(node.left, newVal)
    if node.right:
        printCode(node.right, newVal)
    if not node.left and not node.right:
        print("- %c: %s" % (node.alpha, newVal))
    return

sentence = input("- 문장을 입력하세요: ")
#sentence = "Eerie eyes seen near lake."
dic = {}

for i in range(len(sentence)):
    alpha = sentence[i]
    if alpha in dic:
        dic[alpha] += 1
    else:
        dic[alpha] = 1

dic = sorted(dic.items(), key=lambda x: x[1])
huffman(dic)