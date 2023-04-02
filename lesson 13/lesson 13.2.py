def func1():
    def func2():
        print('hello i am func2')
    return func2()

func1()
