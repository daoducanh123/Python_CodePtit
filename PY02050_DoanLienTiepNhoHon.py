t=  int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    st = list()
    res = [0] * n
    
    for i in range(n):
        while st and arr[st[-1]] <= arr[i]:
            st.pop()    
        if not st:
            res[i] = i + 1
        else:
            res[i] = i -st[-1]
            
        st.append(i)
        
    print(*res)