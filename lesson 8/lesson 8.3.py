def make_operation(operator, *args):
    if operator == '+':
        result = sum(args)
    elif operator == '-':
        result = args[0]-sum(args[1:])
    elif operator == '*':
        result = 1
        for i in args:
            result *= i
    return result

print(make_operation('+', 1,2,3,4))