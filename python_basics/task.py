# Given a list of dicts. Create a new dict with all the values packed 
# in a list if keys in each dict repeats
# flake8: noqa

example = [
    {"a": 123, "b": "hello", "c": True},
    {"a": "word", "f": 0},
    {"a": False, "b": "bye"},
]
dic = {}
for ex in example:
    for e in ex.items():
        lst = dic.setdefault(e[0], [])
        if e[1] not in lst:
            lst.append(e[1]) 

# def func(elem, args=None) -> None:
#     if args is None:
#         args = []
#     args.append(elem)
#     print(args)


# def fibonacci(n):
#     a = 0
#     b = 1

#     for _ in range(n):
#         if a == 0:
#             print(1)
#         c = a + b
#         print(c)
#         a = c
#         a, b = b, a

# fibonacci(5)


lst_1 = ["a", "b", "c"]
lst_2 = [1, 2, 3]
d = dict(zip(lst_1, lst_2))

zipped_pairs = [('x', 1), ('y', 2), ('z', 3)]
letters, numbers = zip(*zipped_pairs)
#  ('x', 'y', 'z') (1, 2, 3)
# because *zip(iter) returns tuples. a, b = *zip([1,2]) returns a = (1,), b = (2,)



exp = {
    "suite.name": "Login Flow",
    "suite.config.browser": "chrome",
    "suite.config.retries": 2,
    "test.id": 101,
    "test.status": "passed"
}

test_info = {
    "suite": {
        "name": "Login Flow",
        "config": {"browser": "chrome", "retries": 2},
    },
    "test": {"id": 101, "status": "passed"},
}

def refine_logs(test_info):
    result = {}
    stack = [test_info, ""] # "" is current path

    current_dict, current_path = stack.pop()

    while stack:
        for key, value in current_dict.items():
            new_path = f"{current_path}.{key}" if current_path else key

            if isinstance(value, dict):
                stack.append((value, new_path))
            else:
                result[new_path] = value

    return result


