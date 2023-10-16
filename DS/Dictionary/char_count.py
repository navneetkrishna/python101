# WAP to count number of occurrences of each character in a given word using dictionary

str = input('Enter a word/string: ')

dic = dict()
for char in str:
    dic[char] = dic.get(char, 0)+1

print(dic)
