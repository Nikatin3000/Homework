name = 'vadim'
name_check = input("Введіть ваше ім'я: ")

if name == name_check or name.title() == name_check:
    print('Вхід дозволено')
else:
    print('Вхід не дозволено')