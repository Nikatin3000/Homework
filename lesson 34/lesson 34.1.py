import threading

class Counter(threading.Thread):

    counter = 0
    rounds = 100000

    def run(self):
        for i in range(Counter.rounds):
            Counter.counter += 1
        return Counter.counter

thread1 = Counter()
thread2 = Counter()

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(thread1.counter)
print(thread2.counter)

