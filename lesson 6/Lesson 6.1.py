import random
num = []
i = 0
while i < 10:
    num.append(random.randint(1, 100))
    i += 1

max_num = num[0]
i = 1
while i < 10:
    if num[i] > max_num:
        max_num = num[i]
    i += 1

print('Список з випадкових чисел', num)
print('Найбільше число з списку', max_num)