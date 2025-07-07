import math
radian = 45 * 3.1415 / 180
print(120 + (72 * math.sin(radian)))
print(120 + (72 * math.cos(radian)))
radian = 90 * 3.1415 / 180
print(math.sin(radian))
print(math.cos(radian))
radian = 135 * 3.1415 / 180
print(math.sin(radian))
print(math.cos(radian))
print(120 - 42)
# from functools import wraps
# def repeat(times):
#     def decorate(fn):
#         @wraps(fn)
#         def wrapper(*args , **kwargs):
#             for _ in range(times):
#                 result = fn(*args , **kwargs)
#             return result
#         return wrapper
#     return decorate
# @repeat(2)
# def say(message):
#     print(message)

# say('hello')

# def star(n):
#     def decorate(fn):
#         def wrapper(*args , **kwargs):
#             print(n*'*')
#             result = fn(*args , **kwargs)
#             print(result)
#             print(n*'*')
#             return result
#         return wrapper
#     return decorate
# @star(5)
# def add(a , b):
#     return a + b
# add(10 , 20)

# class Star:
#     def __init__(self , n):
#         self.n = n
#     def __call__(self, fn):
#         def wrapper(*args , **kwargs):
#             print(self.n*'*')
#             result = fn(*args , **kwargs)
#             print(result)
#             print(self.n*'*')
#             return result
#         return wrapper
# @Star(10)
# def add(a  , b):
#     return a + b
# add(80,20)
# def my_decorator(func):
#     def wrapper():
#         # print('before running function....')
#         func()
#         # print("After running function")    
#     return wrapper
# @my_decorator
# def say_hello():
#     print('Hello world!')
# say_hello()
