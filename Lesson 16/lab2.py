# class Counter:  # Счетчик. Классовое замыкание
#     def __init__(self):
#         self.__counter = 0
#         print("__INIT__")
#
#     def __call__(self, *args, **kwargs):
#         print("__call__")
#         print(args)
#         self.__counter += 1
#         return self.__counter
#
#
# c = Counter()
#
# print(c(1, 2, 3))
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
from pprint import pprint


# class MemoryDecorator:
#     def __init__(self, func):
#         self.func = func
#         self.cache = {}
#
#     def __call__(self, *args, **kwargs):
#         key = (args, frozenset(kwargs.items()))
#         self.cache[key] = self.func(*args, **kwargs)
#         # print(self.cache)
#         return self.cache[key]
#
#     def show_cache(self):
#         pprint(self.cache)
#
#
# @MemoryDecorator
# def sum_num(*args):
#     sum_value = 0
#     for num in args:
#         if isinstance(num, (int, float)):
#             sum_value += num
#         else:
#             raise ValueError(f"Элемент {num} - не является числом")
#     return sum_value
#
#
# mem_dec = MemoryDecorator(sum_num)
# mem_dec(1, 2, 3)
# mem_dec(1, 2, 4, 5)
# mem_dec(1, 2, 4, 5, 66)
#
# # pprint(mem_dec.cache)
#
# sum_num(1, 3, 4, 56, 7, 8)
# sum_num.show_cache()


class Str_decorator:
    def __init__(self, func):
        self.func = func
        self.word_arr = []

    def __call__(self, *args, **kwargs):
        temp_str = self.func(*args, **kwargs)
        self.find_unic_word(temp_str)
        print("Строка успешна изучена")

    def find_unic_word(self, string):
        arr_tpm = string.split()
        print(arr_tpm)
        for word in arr_tpm:
            if word not in self.word_arr:
                self.word_arr.append(word)

    @property
    def wordArr(self):
        return self.word_arr


@Str_decorator
def to_lower(test_str):
    symbols_to_remove = ",!?."
    for symbol in symbols_to_remove:
        test_str = test_str.replace(symbol, "")
    return test_str.lower()


to_lower("Sdfsd sDfsdf! sdfFhj? ghj ghj ghjghj ghj")
print(to_lower.word_arr)
