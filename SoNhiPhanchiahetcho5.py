arr = input().split()

# 0100 1001

LIST = []
for s in arr:
    num = int(s[0]) * (2**3) + int(s[1]) * (2**2) + int(s[2]) * (2**1) + int(s[3]) * (2**0) 

    if num % 5 == 0:
        LIST.append(num)

print(LIST)