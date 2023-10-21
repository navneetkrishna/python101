# # 1.positional argument
#
# def add(a, b):
#     return a + b
#
#
# # print(add(10, 20))
#
#
# # 2. Keyword argument
#
# def division(a, b):
#     return a / b
#
#
# print(division(10, 2))              # name not required
# print(division(10, b=2))            # positional arg then keyword arg
# print(division(a=10, b=2))          # name can be used
# print(division(b=2, a=10))          # order not required if name is used
# # print(division(a=10, 2))          # error, keyword arg can not be used before positional
# # print(division(b=2, 10))          # error, keyword arg can not be used before positional


# # 3. default argument
#
# def wish(msg, user='Guest'):
#     return msg+' '+user
#
#
# print(wish("Hello"))


# # 4. var-length argument
#
# def add(*val):
#     result = 0
#     print(type(val))
#
#     for x in val:
#         result += x
#
#     return result
#
#
# print(add(10, 20, 40))


# 4.2 keyword var-length arguments


