dictionary_1 = {"f_name": 'John', "l_name": 'Wick', "age": 23}

print("Type of dictionary is:", type(dictionary_1))

# Data will be stored in key : value pair in dictionary
print("Initial dictionary values:", dictionary_1)

# -------------------------------------------------------

# retrieve items from dictionary

print("Age of John:", dictionary_1.get("age"))
print(dictionary_1.get("country"))                    # if key is not available, it returns None

# values can be retrieved without using get method if key is not available, it generates error

print(dictionary_1["age"])
# print(dictionary_1["country"])

# -------------------------------------------------------

# adding items to dictionary

dictionary_1["country"] = "UK"
print("Dictionary after adding country", dictionary_1)

# if an already exiting key is added, the item value will be overwritten
# dictionary_1["country"] = "USA"
# print("After updating the country", dictionary_1)


# -------------------------------------------------------

# return a default value if key does not exist

# if corresponding key does not have any value
# provided value can be retrieved as default value


print(dictionary_1.get("city", "London"))
# here London is not stored as item in dictionary

# -------------------------------------------------------
dictionary_1.update({"age": 26})
print("Dictionary with updated age:", dictionary_1)

# -------------------------------------------------------