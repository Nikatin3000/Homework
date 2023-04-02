list1 = []
i = 0
while i <= 100:
    list1.append(i)
    i += 1

list2 = []
i = 0
while i < len(list1):
    if list1[i] % 7 == 0 and list1[i] % 5 != 0:
        list2.append(list1[i])
    i += 1

print('Список від 1 до 100',list1)
print('Числа які діляться на 7 но не кратні 5',list2)