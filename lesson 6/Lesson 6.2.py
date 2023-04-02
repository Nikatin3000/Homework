import random

list1 = []
i = 0

while i < 10:
    list1.append(random.randint(1, 10))
    i += 1

list2 = []
i = 0

while i < 10:
    list2.append(random.randint(1, 10))
    i += 1


list3 = []
i = 0
while i < 10:
      if list1[i] in list2 and list1[i] not in list3:
          list3.append(list1[i])
      i += 1

print('Перший список:',list1)
print('Другий список:',list2)
print('Загальні числа без дублікатів:',list3)
