class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        newNode = Node(data)
        if (self.tail == None):
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def dequeue(self):
        if (self.head == None):
            return None
        else:
            val = self.head.data
            self.head.data = None
            self.head = self.head.next
            self.head.prev.next = None
            self.prev = None
            return val

    def topVal(self):
        return self.head.val

    def bottomVal(self):
        return self.tail.val

    def isEmpty(self):
        return (self.head == None)

    def display(self):
        cur = self.head
        while cur != None:
            print(cur.data,end=" ")
            cur = cur.next
        print()
