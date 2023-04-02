# def oops():
#     raise KeyError("Index error, not good.") - буде помилка Traceback (most recent call last)

def oops():
    raise IndexError("Index error, not good.")

def oops2():
    try:
        oops()
    except IndexError as a:
        print(f"Caught an IndexError: {a}")

oops2()