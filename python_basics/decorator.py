import time


def log_time(func):

    def wrapper(*args):
        print(f"Start time: {time.perf_counter()}")
        func(*args)
        print(f"End time: {time.perf_counter()}")

    print("Inside decorator")
    return wrapper


@log_time
def iterate_over_list(num: int):
    print("Inside iterating function")
    for el in range(1, num):
        print(el)
    print("End of iterating")


iterate_over_list(12)
