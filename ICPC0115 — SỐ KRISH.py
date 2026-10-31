def Factorial(number):
    f = 1
    for i in range(1, number+1):
        f *= i
    return f
def Sum(s):
    sum = 0
    for i in range(len(s)):
        number = int(s[i])
        f = Factorial(number)
        sum += f
    return sum
t = int(input())
for _ in range(t):
    s = input()
    ognumber = int(s)
    if Sum(s) == ognumber:
        print("Yes")
    else:
        print("No") 
    