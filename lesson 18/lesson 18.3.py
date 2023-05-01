from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func1 = func(*args, **kwargs)
            try:
                return int(func1)
            except ValueError:
                return func1
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func1 = func(*args, **kwargs)
            try:
                return str(func1)
            except ValueError:
                return func1
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func1 = func(*args, **kwargs)
            try:
                return float(func1)
            except ValueError:
                return func1
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func1 = func(*args, **kwargs)
            return bool(func1)
        return wrapper


@TypeDecorators.to_float
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string

@TypeDecorators.to_str
def do_somethi(string: str):
    return string

assert do_somethi(25) == '25'
assert do_nothing('25') == 25
assert do_something('True') is True