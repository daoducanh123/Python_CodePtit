n,m = map(int,input().split())

a= list(map(int,input().split()))

ops = ['+','-', '*']
ans = [] 

def back(i,expr,total,last):
    if i == n:
        if total == m:
            ans.append(expr + '=' + str(m))
        return
    x= a[i]
    
    
    back(i+1,expr+'+'+str(x),total+x,x)
    back(i+1,expr + '-' + str(x), total-x,-x)
    new = total - last + last * x
    back (i+1,expr+'*' + str(x), new , last*x)
back(1,str(a[0]),a[0],a[0])
if ans :
    print('\n'.join(ans))
else:
    print   ('IMPOSSIBLE')