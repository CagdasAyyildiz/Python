def decorator(func):

    def inner():
        print("decorated now")
        func()
        print("decorated now")
    return inner


@decorator
def decorated_function():
    print("normal function")


decorated_function()