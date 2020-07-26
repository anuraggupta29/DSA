class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        newNode = Node(data)

        if (self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def deleteNode(self, position):
        cur = self.head
        if not self.head:
            break
        elif position == 0:
            self.head = self.head.next
        else:
            for i in range(position-1):
                cur = cur.next

            if cur.next == self.tail:
                self.tail = cur

            cur.next = cur.next.next

    def printLinkedList(self):
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.data)
            cur = cur.next

        return arr

llist = SinglyLinkedList()
llist.addNode(1)
llist.addNode(2)
llist.addNode(3)
llist.addNode(4)
llist.addNode(5)
llist.deleteNode(2)
print(llist.printLinkedList())
