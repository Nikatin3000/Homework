class Open_file:
    def __init__(self, name, method):
        self.name = name
        self.method = method
        self.file = None
        self.counter = 0

    def __enter__(self):
        self.file = open(self.name, self.method)
        self.counter += 1
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.counter -= 1
        if self.counter == 0:
            self.file.close()


with Open_file('test lesson 21.txt', 'w') as file: # для запису
    file.write('Hello, world!')
# with Open_file('test lesson 21.txt', 'r') as file: # для читання
    # print(file.read())