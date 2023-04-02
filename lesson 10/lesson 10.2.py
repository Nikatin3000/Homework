def input_user():
    try:
        a = int(input('Введіть перше число: '))
        b = int(input('Введіть друге число: '))
        result = a ** 2 / b
        return result
    except ValueError:
        print('упс, ви ввели не число')
    except ZeroDivisionError:
        print('на 0 ділити не можна')

print(input_user())