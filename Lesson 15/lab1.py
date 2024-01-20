# def outer():  # Замыкание. Счетчик
#     n = 0
#
#     def inner():
#         nonlocal n
#         n += 1
#         print(n)
#
#     return inner
#
#
# fn = outer()
# fn()
# fn()
# fn()
# fn()
# fn()


# class OuterClass():  # Замыкание. Счетчик с помощью класса
#     def __init__(self):
#         self.n = 0
#
#     def inner(self):
#         self.n += 1
#         print(self.n)
#
#
# Cls = OuterClass()
# Cls.inner()
# Cls.inner()
# Cls.inner()
# Cls.inner()


# def multiply(n):
#
#     def inner(m):
#         return n*m
#
#     return inner
#
#
# fn = multiply(5)
#
# print(fn(10))
# print(fn(20))
# print(fn(30))
# print(fn(40))

# import random
# import string
#
#
# def password_gen(length):
#     def gen_pass():
#         characters = string.ascii_letters + string.digits + string.punctuation
#         password = "".join([random.choice(characters) for i in range(length)])
#         print(password)
#         return password
#     return gen_pass
#
#
# fn = password_gen(28)
# fn()
# fn()
# fn()
# fn()

#
# def action(znak, num1):
#     def plus_minus(num2):
#         return num1 - num2 if znak == "-" else num1 + num2
#     return plus_minus
#
#
# rt = action("+", 12)
# print(rt(10))
# print(rt(15))
# print(rt(5))
# rt = action("-", 13)
# print(rt(10))
# print(rt(15))
# print(rt(5))


# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("*" * 10)
#         func(*args, **kwargs)
#         print("*" * 10)
#
#     return wrapper
#
#
# @func_decorator
# def test():
#     print("Hello World")
#
#
# @func_decorator
# def test2(name):
#     print("Hello", name)
#
#
# # fn = func_decorator(test)
# # fn()
# # fn2 = func_decorator(test2)
# # fn2()
# test()
# test2("Tom")

import time
import sys
sys.setrecursionlimit(1000000)


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        # print(st)
        res = func(*args, **kwargs)
        end = time.time()
        # print(end)
        dt = end - st
        print(f"Время работы: {dt}")
        return res
    return wrapper


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# print(time.time())
# print(factorial(5))
# factorial(10)
fn = test_time(factorial)
fn(900)
fn(9000)
fn(90000)
fn(200000)
