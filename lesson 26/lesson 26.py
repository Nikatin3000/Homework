def binary_search(data, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if data[mid] == x:
            return mid

        elif data[mid] > x:
            return binary_search(data, low, mid - 1, x)

        else:
            return binary_search(data, mid + 1, high, x)

    else:
        return -1



# data = [2, 10, 3, 4, 50, 40]
# x = 10
#
# res = binary_search(data, 0, len(data)-1, x)
# print(res)

def fibonacci_search(data, x):
    n = len(data)
    m2, m1 = 0, 1
    fib_m = m2 + m1
    while fib_m < n:
        m2, m1 = m1, fib_m
        fib_m = m2 + m1

    offset = -1
    while fib_m > 1:
        i = min(offset + m2, n - 1)
        if data[i] < x:
            fib_m, m1 = m1, m2
            m2 = fib_m - m1
            offset = i
        elif data[i] > x:
            fib_m, m1 = m2, m1 - m2
            m2 = fib_m - m1
        else:
            return i
    if m1 == 1 and data[offset + 1] == x:
        return offset + 1
    return -1


# data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# x = 18
# index = fibonacci_search(data, x)
# print(index)