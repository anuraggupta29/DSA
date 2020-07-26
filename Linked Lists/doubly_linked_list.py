class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,data):
        newNode = Node(data)

        if (self.head == None):
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def display(self):
        cur = self.head
        while (cur != None):
            print(cur.data,end=" ")
            cur = cur.next
        print()

    def newHead(self,data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode

        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insertAfter(self,givenNode,data):
        newNode = Node(data)
        newNode.next = givenNode.next
        newNode.next.prev = newNode
        givenNode.next = newNode
        newNode.prev = givenNode

    def insertBefore(self,givenNode,data):
        if (givenNode == self.head):
            self.newHead(data)
        else:
            self.insertAfter(givenNode.prev,data)

    def removeNode(self,givenNode):
        if (givenNode == self.head):
            self.head = givenNode.next
            self.head.prev = None
            givenNode.data = None
            givenNode.next = None

        elif (givenNode == self.tail):
            self.tail = givenNode.prev
            givenNode.data = None
            givenNode.prev = None
        else:
            givenNode.prev.next = givenNode.next
            givenNode.next.prev = givenNode.prev
            givenNode.next = None
            givenNode.prev = None
            givenNode.data = None

    def random(self):
        cur = self.head
        arr = []
        while cur != None:
            arr.append(cur)
            cur = cur.next

        return arr[random.randint(0, len(arr)-1)]

#TEST---------------------------------------------------------------------------
a = DLL()

for i in range(10):
    a.addNode(i)

a.display()
a.newHead(21)
a.display()
a.insertAfter(a.head.next.next,34)
a.display()
a.insertBefore(a.head.next.next.next.next.next,67)
a.display()
a.removeNode(a.head)
a.display()
