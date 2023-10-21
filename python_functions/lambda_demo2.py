# Program to filter only even numbers
# from the list by using filter() function
#
# # example without lambda expression
#
# def isEven(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# l = [0, 5, 10, 15, 20, 25, 30]
# l1 = list(filter(isEven, l))
# print(l1)  # [0,10,20,30]

# -----------------------

# with lambda expression

l3 = [0, 5, 10, 15, 20, 25, 30]
l4 = list(filter((lambda x: x % 2 == 0), l3))
print(l4)
