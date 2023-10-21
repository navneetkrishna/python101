# sample_file = "./sample.txt"
#
# my_file = open(sample_file, 'r')
#
# print(my_file.read())
#
# # always close the file after use.
# my_file.close()

# ------------------------------------------
# seek()

sample_file = "./sample2.txt"

file = open(sample_file, 'r+')
print(file.read())

# move pointer to beginning
file.seek(0)
print("------Break here------")
print(file.read())

print("------Break here------")

file.close()


# ------------------------------------------
# # readlines() function
#
# sample_file = "./sample.txt"
#
# my_file = open(sample_file, 'r')
#
# print(my_file.readlines())
#
# # always close the file after use.
# my_file.close()





