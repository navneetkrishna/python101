# basic function
def my_function(num1, num2):
    return num1 + num2


# print("Sum of 20 and 30 is:", my_function(20, 30))

# --------------------------------------------------

# default parameter function
def default_param_function(num1, num2=100):
    print("1st number is:", num1)
    print("2nd number is:", num2)


# default_param_function(20)
# default_param_function(20, 50)
# # default_param_function(20, 30)      # works same as line 6

# -----------------------------------

# keyword call

def keyword_function(num1, num2):
    print("1st number is:", num1)
    print("2nd number is:", num2)

#
# keyword_function(num1=10, num2=20)
# keyword_function(10, 20)

