class Stack:
    def __init__(self,arr = []):
        self.arr = arr

    def pop(self):
        return self.arr.pop()

    def push(self,data):
        self.arr.append(data)

    def isEmpty(self):
        return (len(self.arr) == 0)

    def peek(self):
        return self.arr[0]

s1 = Stack()
s1.push(2)
s1.push(5)
s1.pop()
print(s1.peek())
