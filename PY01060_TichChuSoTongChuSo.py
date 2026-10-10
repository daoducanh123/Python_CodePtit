t = int(input())
for _ in range(t):
    sum =0
    mul = 1
    string = input()
    for i in range(len(string)):
        number= int(string[i])
        if i % 2 == 0 and number != 0:
            mul *= number
        elif i % 2 ==1:
            sum += number
            
    print(f"{mul} {sum}")