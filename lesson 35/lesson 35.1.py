import concurrent.futures
import math

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def filter_threadpool(numbers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(is_prime, numbers)
    return list(results)

def filter_processpool(numbers):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(is_prime, numbers)
    return list(results)

threadpool_results = filter_threadpool(NUMBERS)

processpool_results = filter_processpool(NUMBERS)

print("Результати виконання з використанням ThreadPoolExecutor:")
for number, is_prime in zip(NUMBERS, threadpool_results):
    print(f"{number}: {'просте' if is_prime else 'не просте'} число")

print("\nРезультати виконання з використанням ProcessPoolExecutor:")
for number, is_prime in zip(NUMBERS, processpool_results):
    print(f"{number}: {'просте' if is_prime else 'не просте'} число")
