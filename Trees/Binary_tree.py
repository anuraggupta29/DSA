class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.head = None
        self.total = 0

    def insert(self,data):
        newNode = Node(data)
        if (self.head is None):
            self.head = newNode
            self.total = 1
        else:
            cur = self.head
            while True:
                if newNode.data > cur.data:
                    if cur.right is None:
                        cur.right = newNode
                        self.total += 1
                        break
                    else:
                        cur = cur.right
                elif newNode.data < cur.data:
                    if cur.left is None:
                        cur.left = newNode
                        self.total += 1
                        break
                    else:
                        cur = cur.left
                else:
                    break

    def _printTree(self,cur):
        if cur.left:
            self._printTree(cur.left)
        print(cur.data, end=" ")
        if cur.right:
            self._printTree(cur.right)

    def printTree(self):
        cur = self.head
        self._printTree(cur)

    def totalNodes(self):
        return self.total

b = BinarySearchTree()
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(1.4)
b.insert(0)
print(b.head.right.left.data)
b.totalNodes()
b.printTree()
