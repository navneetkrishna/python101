my_list = ['1', 1, 29.5, 'Dell', 'HP', ['abc', 'def']]

print(my_list)

print(type(my_list))                        # prints the class(data type) of the variable

print(len(my_list))                         # prints the length of the list

my_list.append('Apple')                     # append an element to the list
print(my_list)

print(my_list.pop())                        # pop will remove and return the last element

my_list.remove(['abc', 'def'])              # removes specified element
print(my_list)


# ------------------------------------------------------------------------------------

# MY_STR = "To be or not to be, that is the question"
#
# print(len(MY_STR))                                 # length of the string
#
# print(MY_STR.split(' '))                           # string words split into list
# print(len(MY_STR.split(' ')))                      # length of word list
#
# print(list(MY_STR))                                # string characters split into list
