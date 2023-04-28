class MyIter:
    def __init__(self,data):
        self.data = data
        self. index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            result = self.data[self.index]
            self.index += 1
            return  result

    def __getitem__(self, index):
        return self.data[index]

my_iter = MyIter([1,2,3,4,5,6,7])
for _ in my_iter:
    print(_)