class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnorderedList:
    def __init__(self):
        self.head = None

    def append(self, i):
        new_node = Node(i)
        new_node.next = self.head
        self.head = new_node

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        return -1

    def pop(self):
        current = self.head
        previous = None
        while current.next is not None:
            previous = current
            current = current.next
        if previous is None:
            self.head = None
        else:
            previous.next = None
        return current.data

    def insert(self, pos, i):
        if pos == 0:
            self.append(i)
        else:
            new_node = Node(i)
            current = self.head
            previous = None
            index = 0
            while current is not None and index < pos:
                previous = current
                current = current.next
                index += 1
            new_node.next = current
            previous.next = new_node

    def slice(self, start, stop):
        new_list = list()
        current = self.head
        index = 0
        while current is not None and index < stop:
            if index >= start:
                new_list.append(current.data)
            current = current.next
            index += 1
        return new_list


unorderedlist = UnorderedList()
unorderedlist.append(1)
unorderedlist.append(2)
unorderedlist.append(3)
unorderedlist.append(4)
index_of_3 = unorderedlist.index(3)
print(index_of_3)
last_item = unorderedlist.pop()
print(last_item)
unorderedlist.insert(1, 5)
print(unorderedlist.slice(0, 4))
new_list = unorderedlist.slice(0, 2)
print(new_list)
