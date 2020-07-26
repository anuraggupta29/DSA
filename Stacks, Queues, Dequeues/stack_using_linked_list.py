class stackNode:
    def __init__(self, data):
        self.data = data
        self.prev = None

class StackLL:
    def __init__(self):
        self.tail = None

    def push(self, data):
        node = stackNode(data)
        if self.tail == None:
            self.tail = node
        else:
            node.prev = self.tail
            self.tail = node

    def pop(self):
        if self.tail != None:
            out = self.tail
            self.tail = self.tail.prev
            return out.data

    def displayStack(self):
        node = self.tail
        arr = []
        while node:
            arr.append(node)
            node = node.prev
        return arr, [i.data for i in arr]

x = StackLL()
x.push(1)
x.push(3)
x.push(8)
x.push(6)
print(x.displayStack()[1])
x.pop()
x.pop()
print(x.displayStack()[1])
