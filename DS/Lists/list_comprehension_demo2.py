# WAP to generate a list
# which contains squares of first 20 numbers.
# and print only even numbers from the list

# list = [ {expression} for x in sequence if condition]

lst1 = [x*x for x in range(1, 21)]                   # square list
print(lst1)

lst2 = [x for x in lst1 if x % 2 == 0]      # even list
print(lst2)
