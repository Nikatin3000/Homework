"add called with 4, 5"



def logger(func):
    def adder(*args):
        print(f'{func.__name__} called with: {args}')
    return adder


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4,5)
square_all(2,3,4)