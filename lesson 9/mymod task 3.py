def count_lines(name):
    f = open(name, 'r')
    return len(f.readlines())

def count_chars(name):
    t = open(name, 'r')
    return len(t.read(-1))

def test(name):
    num_lines = count_lines(name)
    num_chars = count_chars(name)
    print(f"Кількість рядків: {num_lines}")
    print(f"Кількість символів: {num_chars}")
    print(f"Назва файлу: {name}")
    return

test('mymod.py')

