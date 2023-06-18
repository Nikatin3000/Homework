# import asyncio
#
# async def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         sequence = [0, 1]
#         for i in range(2, n):
#             next_num = sequence[i-1] + sequence[i-2]
#             sequence.append(next_num)
#         return sequence
#
# async def factorial(n):
#     if n < 0:
#         return None
#     elif n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n+1):
#             result *= i
#         return result
#
# async def squares(n):
#     return [i**2 for i in range(1, n+1)]
#
# async def cubes(n):
#     return [i**3 for i in range(1, n+1)]
#
# async def calculate_results():
#     tasks = []
#     for i in range(1, 11):
#         fib_task = asyncio.create_task(fibonacci(i))
#         fact_task = asyncio.create_task(factorial(i))
#         square_task = asyncio.create_task(squares(i))
#         cube_task = asyncio.create_task(cubes(i))
#         tasks.extend([fib_task, fact_task, square_task, cube_task])
#     results = await asyncio.gather(*tasks)
#     fib_results = results[0:40:4]
#     fact_results = results[1:40:4]
#     square_results = results[2:40:4]
#     cube_results = results[3:40:4]
#     return fib_results, fact_results, square_results, cube_results
#
# fib_results, fact_results, square_results, cube_results = asyncio.run(calculate_results())
#
# print("Fibonacci:", fib_results)
# print("Factorial:", fact_results)
# print("Squares:", square_results)
# print("Cubes:", cube_results)

import multiprocessing

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_num = sequence[i-1] + sequence[i-2]
            sequence.append(next_num)
        return sequence

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

def squares(n):
    return [i**2 for i in range(1, n+1)]

def cubes(n):
    return [i**3 for i in range(1, n+1)]

def calculate_results():
    with multiprocessing.Pool() as pool:
        results = pool.map_async(fibonacci, range(1, 11))
        fib_results = results.get()

        results = pool.map_async(factorial, range(1, 11))
        fact_results = results.get()

        results = pool.map_async(squares, range(1, 11))
        square_results = results.get()

        results = pool.map_async(cubes, range(1, 11))
        cube_results = results.get()

    return fib_results, fact_results, square_results, cube_results


if __name__ == '__main__':
    fib_results, fact_results, square_results, cube_results = calculate_results()
    print("Fibonacci:", fib_results)
    print("Factorial:", fact_results)
    print("Squares:", square_results)
    print("Cubes:", cube_results)

# multiprocessing виграє на дистанції, чим більше данних і чим важче обчислення тим більша ефективність над asyncio