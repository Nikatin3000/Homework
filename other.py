import random

def r1():
    return random.randint(0, 10)

def r2():
    return random.randint(0, 100)

def r3():
    return random.randint(0, 300)
# задача 1
def main(func1, func2, func3):
    list1 = []
    if func1()% 2 == 0:
        list1.append(func1)
    if func2()% 2 == 0:
        list1.append(func2)
    if func3()% 2 == 0:
        list1.append(func3)
    return list1
# задача 2
def main2(*args):
    list2 = []
    for arg in args:
        if arg % 2 == 0:
            list2.append(args)
        return list2

print(main2(r1(),r2(),r3()))

# def main2(*args):
#     list2 = []
#     [list2.append(arg) for arg in args if arg % 2 == 0]
#     return list2

# print(main(r1,r2,r3))
# print(hex(id(main)))



