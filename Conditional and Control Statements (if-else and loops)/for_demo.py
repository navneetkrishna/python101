# myList = ["car", "house", "bike", "boat"]
#
# for i in myList:
#     print(i)
# -------------------------------------------
# for i in range(5):
#     print(i)
#
# # for i in range(2, 5): to iterate from 2 to 5

# --------------------------------------------

quote = "Give a man a program, frustrate him for a day. Teach a man program, frustrate him for a lifetime."

# # tokens = quote.split()
#
# for i in quote.split():
#     print(i)

# --------------------------------------------

# Task: if the token is more than(or equal) 3 characters, then collect it into list and print

quote_list = []

for i in quote.split():

    if len(i) <= 3:
        # print(type(quote_list))
        quote_list.append(i)

print(quote_list)

