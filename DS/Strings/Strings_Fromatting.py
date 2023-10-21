
MY_STR = "To be or not to be, that is the question"

print(len(MY_STR))                                 # length of the string

print(MY_STR.split(' '))                           # string words split into list
print(len(MY_STR.split(' ')))                      # length of word list

print(list(MY_STR))                                # string characters split into list
# --------------------------------------------------------------

# python 3.7 >

# prg = 'Python'
#
# print(f'I know {prg} programming language')     # use f before string (without space)
#
# print(f'I know {prg} programming language since {prg.__len__()}')

# ------------------------------------------------------------

# python 3
# str = "{} is {} years old"
# str2 = "I know {} programming language"
# str3 = "{name} is {age} years old. He has {money} dollars"
#
# print(str.format('Jhon', 22))
# print(str2.format("Python"))
# print(str3.format(name = 'Jhon', age = 22, money = 12.99))

# ------------------------------------------------------------
# python 2
# won't work in python 3
#
# str_2 = "%s is %d years old. He has %f dollars"
#
# print(str_2.format('Jhon', 22, 10.29))