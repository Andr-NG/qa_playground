# flake8: noqa





def decorator_func(fun):

    print("Inside decorator func")

    def wrapper(*args):
        print(f"Inside wrapper function: {wrapper.__name__}")
        fun(*args)
        print(f"{fun} executed. Leaving wrapper")
    return wrapper


@decorator_func
def print_input_numbers(*args):
    print(f"Inside {print_input_numbers.__name__}")
    for arg in args:
        print(arg)



print_input_numbers(1, 3, 5, 7, 9)