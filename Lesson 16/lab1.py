# def decorator(func):
#     def wrapper(*args, **kwargs):
#         # print(args)
#         # print(kwargs)
#         print("Начало декоратора")
#         func(*args, **kwargs)
#         print("Конец декоратора")
#
#     return wrapper
#
#
# @decorator
# def test_function(name, second_mess, lowercase=False):
#     if lowercase:
#         print(f"Hello,{name}!{second_mess}".lower())
#     else:
#         print(f"Hello,{name}!{second_mess}")
#
#
# # dec1 = decorator(test_function)
# # dec1("Tom", "Have a good day", lowercase=True)
#
#
# test_function("Tom", "Have a good day", lowercase=True)


def memory_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        # print(frozenset(kwargs.items()))
        key = (args, frozenset(kwargs.items()))
        cache[key] = func(*args, **kwargs)
        print(cache)
        return cache[key]

    return wrapper


@memory_decorator
def sum_num(*args):
    sum_value = 0
    for num in args:
        if isinstance(num, (int, float)):
            sum_value += num
        else:
            raise ValueError(f"Элемент {num} - не является числом")
    return sum_value


print(sum_num(1, 2, 3, 4, 5, 6, 7))
print(sum_num(1, 2, 3, 4, 5, 6, 7, 8, 9))

