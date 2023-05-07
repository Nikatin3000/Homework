# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self,a):
#         return self.stack.append(a)
#
#     def pop(self):
#         return self.stack.pop()
#
#     def pick(self):
#         return self.stack[-1]
#
#     def isempty(self):
#         return not bool(self.stack)
#
#     def size(self):
#         return len(self.stack)
#
#     def get_from_stack(self,e):
#         if e not in self.stack:
#             raise ValueError('елемент не знайдено')
#         index = self.stack.index(e)
#         return self.stack.pop(index)
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
#
# print(stack.get_from_stack(2))  # 2
# print(stack.get_from_stack(4))  # 4
# print(stack.get_from_stack(5))  # ValueError: 5 not found in stack

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue_right(self, a):
        return self.queue.append(a)

    def enqueue_left(self, a):
        return self.queue.insert(0,a)

    def dequeue_right(self):
        return self.queue.pop(-1)

    def dequeue_left(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return not bool(self.queue)

    def size(self):
        return len(self.queue)

    def get_from_stack(self, e):
        if e not in self.queue:
            raise ValueError('елемент не знайдено')
        index = self.queue.index(e)
        res = self.queue.pop(index)
        self.queue = self.queue[:index] + self.queue[index:]
        return res

queue = Queue()
queue.enqueue_right(2)
queue.enqueue_right(6)
queue.enqueue_right(8)
queue.enqueue_right(9)
queue.enqueue_left(33)
print(queue.get_from_stack(2))
print(queue.get_from_stack(6))
print(queue.get_from_stack(21))