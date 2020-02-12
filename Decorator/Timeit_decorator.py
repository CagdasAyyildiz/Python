import timeit
import time


def timing(func):
    def inner():
        start_time = timeit.default_timer()
        func()
        stop_time = timeit.default_timer()
        print("Elapsed time with timeit module", stop_time - start_time)

    return inner


@timing
def do_something():
    time.sleep(3)


do_something()