def with_index(iterable,start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1


l = ["перший", "другий", "третій"]
print(list(with_index(l,1)))

