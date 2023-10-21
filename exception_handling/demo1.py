# # try:
# #     div = 5 / 0
# #
# # except:
# #     print("Dont divide by 0")

# # Nested-Exception example
#
# my_list = ["car", "bike", "house", "boat"]
#
# try:
#     print(my_list[5])
#     div = 5 / 0
#
# # line 11 will not be executed as  control will jump out of the try block at line 10
#
# except IndexError as e:
#
#     print(f"You got {e} error")
#
# except ZeroDivisionError as e:
#     print(f"You got {e} error")

# re-raise exception

try:
    div = 5 / 0

except ZeroDivisionError as e:
    print(f"You got {e} error")
    raise ZeroDivisionError("Reraised the zeroDivision error")




# Python code to show how to raise an exception in Python
num = [3, 4, 5, 7]
if len(num) > 3:
    raise Exception( f"Length of the given list must be less than or equal to 3 but is {len(num)}")


