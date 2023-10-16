# WAP to generate a list
# which contains squares of first 10 numbers.
# list = [ {expression} for x in sequence]

lst = []

for x in range(1,11):
    lst.append(x*x)
print(lst)

lst2 = [x*x for x in range(1,11)]
print(lst2)

