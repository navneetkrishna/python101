sample_file = "./Demo.txt"
my_string = "Hi, how are you?\n"
my_string1 = "Hope you are doing well!\n"

# Example 1

# with open(sample_file, 'a+') as f:
#     f.write(my_string)
#     f.write(my_string1)
#     f.seek(0)
#     print(f.read())


# Example 2

users_list = ['John', 'Doe', 'Max', 'Sam']

with open(sample_file, 'a+') as f:

    # f.write(users_list)             # write() accepts only string

    for i in users_list:

        f.write(i + '\n')
        f.seek(0)

    print(f.read())