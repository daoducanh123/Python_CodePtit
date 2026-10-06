t = int(input())
for _ in range(t):
    n = int(input())
    arrInput = input().split()
    
    arrSum = list()
    for a in arrInput:
        num = int(a)
        sum = 0
        for aa in a:
            sum += int(aa)
        arrSum.append([num,sum])
    
    arrSum = sorted (arrSum, key = lambda x: x[0])
    arrSum = sorted (arrSum, key = lambda x: x[1])
    
    for i in range(len(arrSum)):
        print(arrSum[i][0] , end=" ")
    
    print()