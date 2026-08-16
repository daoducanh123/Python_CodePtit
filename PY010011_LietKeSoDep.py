def CheckChan(num):
    for n in num:
        if n not in "02468":
            return False
    return True

def CheckSoLuongChan(num):
    return len(num) % 2 == 0

def CheckThuanNghich(num):
    return num == num[::-1]

#main
test = int(input())
while(test > 0):
    num = input()

    for x in range(2,int(num),2):
        x = str(x)
        if CheckChan(x) == True and CheckSoLuongChan(x) == True and CheckThuanNghich(x) == True:
            print(f"{x}", sep = "", end = " ")
    print()
    test -= 1

