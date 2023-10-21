# # WAP using lambda function
# # to square a given value
#
# # syntax => lambda arg_list: (expression)
# # ex:       lambda (a, b): (a+b)
#
# s = lambda num: num*2
# print(s(4))
#
# add = lambda v1, v2: (v1 + v2)
# print(add(4, 2))
#
#

# WAP to find biggest of 2 numbers

large = lambda n1, n2: (n1 if n1 > n2 else n2)
print(large(70, 80))

