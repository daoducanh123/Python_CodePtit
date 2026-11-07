n,m = map(int,input().split())

a = []

for i in range(n):
    a.append(list(map(int,input().split())))
    
def is_palindrome(x):
    s= str(x)
    return len(s) >= 2 and s == s[::-1]

max_palindrome = -1


for i in range(n):
    for j in range(m):
        if is_palindrome(a[i][j]):
            max_palindrome =  max(max_palindrome,a[i][j])
            
if max_palindrome == -1:
    print("NOT FOUND")
    
else:
    print(max_palindrome)
    
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_palindrome:
                print(f"Vi tri [{i}][{j}]")