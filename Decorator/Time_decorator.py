import time


def timing(func):
    def inner():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("Elapsed time with time module", stop_time - start_time)

    return inner


@timing
def do_something():
    time.sleep(3)


do_something()
