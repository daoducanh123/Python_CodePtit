str1 = input()
str2 = input()
p = int (input())

# print (f"{str1[0:p-1]}{str2}{str1[p-1:len(str1)]}")
print (f"{str1[:p-1]}{str2}{str1[p-1:]}")