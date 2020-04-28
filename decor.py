def print_func(func):
    def wrapper(*args):
        print(func(*args))
    return wrapper

123