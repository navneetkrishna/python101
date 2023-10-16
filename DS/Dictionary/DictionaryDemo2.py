dictionary_2 = {"a": 47, "b": 48}
# print(dictionary_2)


# Get all key & values
print(dictionary_2.keys())
print(dictionary_2.values())

# ----------------------------------------------------------
# Dictionary setdefault() function

# it inserts a key with the default value to the dictionary.
dictionary_2.setdefault("c", 50)
print(dictionary_2)

# returns the value of a key (if the key is in dictionary).

print(dictionary_2.setdefault("c"))