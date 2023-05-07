# a = [1,2,3,4,5,6,7,8,9,10]
#
# def reverse(a):
#     return a.reverse()
#
#
# reverse(a)
# print(a)

class Stack:
    def __init__(self):
        self.a = [1,2,3,4,5,6,7,8,9,10]

    def reverse(self):
        return self.a.reverse()

stack = Stack()
stack.reverse()
print(stack.a)