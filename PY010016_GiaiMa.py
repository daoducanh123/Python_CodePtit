test = int(input())
for t in range(0,test):
    num = input()
    for i in range(0,len(num)-1,2):
        cnt = int(num[i+1])
        while(cnt > 0):
            print(num[i],end="")
            cnt -= 1

    print()