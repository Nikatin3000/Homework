# Task1

def to_power(x, exp: int):
    if exp == 1:
        return x
    if exp == 0:
        return 1
    elif exp < 0:
        raise ValueError('Степінь меньше 0')
    else:
        return x * to_power(x, exp-1)


# print(to_power(2, 3))
# print(to_power(3.5, 2))
# print(to_power(2, -1))

# Task 2

def is_palindrome(looking_str: str) -> bool:
    if len(looking_str) <= 1:
        return True
    if looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])

# print(is_palindrome('mom'))
# print(is_palindrome('sassas'))
# print(is_palindrome('o'))
# print(is_palindrome('qwer'))

# Task 3

from typing import Optional
def mult(a: int, n: int) -> int:
    if n < 0:
        raise ValueError("This function works only with postive integers")
    if n == 0:
        return 0
    return a + mult(a,n-1)

# print(mult(2, 4))
# print(mult(2, 0))
# print(mult(2, -4))

# Task 4

def reverse(input_str: str) -> str:
    if len(input_str) == 1:
        return input_str
    return reverse(input_str[1:]) + input_str[0]

# print(reverse("hello"))
# print(reverse("o"))

# Task 5

def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")
    if len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])

# print(sum_of_digits('26'))
# print(sum_of_digits('test'))



