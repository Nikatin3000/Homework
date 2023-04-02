name = input('Введіть слово: ')


if len(name) >= 2:
    print(name[:2] + name[-2:])
else:
    print('empty string')
