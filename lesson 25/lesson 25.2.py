class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.stack = None

    def push(self,data):
        data_node = Node(data)
        data_node.next = self.stack
        self.stack = data_node


    def pop(self):
        if self.is_empty():
            return None
        data = self.stack.data
        self.stack = self.stack.next
        return data

    def is_empty(self):
        return self.stack is None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())
