import random

user = input('Введіть строку: ')
len_string = len(user)

for i in range(5):
    random_string = ''
    for j in range(len_string):
        random_index = random.randint(0, len_string - 1)
        random_string += user[random_index]
    print(random_string)



