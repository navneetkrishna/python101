# take this input from user
# {1: 100, 2: 200, 3: 300}
# print sum of values

# dic = eval(input('Enter key-value: '))
# print(type(dic))
# print(dic)
#
#
# s = 0
#
# for values in dic.values():
#     s += values
#
# print(s)

# above can be minimized as

dic = eval(input('Enter key-value: '))

s1 = sum(dic.values())
print('Sum:', s1)



