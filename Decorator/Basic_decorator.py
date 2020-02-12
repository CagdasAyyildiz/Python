def decorator(func):
    def inner():
        print("breakpoint1")
        func()
        print("breakpoint2")

    return inner


@decorator
def decorated():
    print("do something")


decorated()
