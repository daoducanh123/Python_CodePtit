import sys 

def solve():
    data= sys.stdin.read().split()
    if not data:
        return
    m = int(data[0])
    d = int(data[1])
    a = data[2]
    b=data[3]
    mod = 10**9+7


    def count(s):
        dp = {(0,1):1}
        for i , ch in enumerate(s):
            nxt = {}
            limit = int(ch)
            if i % 2==1:
                digits = [d]
            else:
                start = 1 if i == 0 else 0
                digits = [
                    c for c in range(start,10)
                    if c!=d
                ]

            for (rem,tight), ways in dp.items():
                if tight:
                    maxc = limit
                else:
                    maxc= 9

                for c in digits:
                    if c > maxc:
                        continue
                    nrem = (rem*10+c) % m
                    if tight and  c == limit:
                        ntight=1
                    else:
                        ntight = 0

                    key = (nrem,ntight)


                    nxt[key] = (
                        nxt.get(key,0) + ways
                    )%mod
            dp = nxt
        return(
            dp.get((0,0),0) + dp.get((0,1),0)) % mod
    

    valida= (sum(
        1
        for i,c in enumerate(a)
        if(
            (i%2 == 1 and int(c)!=d)
            or
            (i%2 == 0 and int(c) == d)
        )
    ) == 0
    and int(a)% m == 0
    )
    print(
        (count(b)-count(a) + valida)% mod
    )

if __name__ == '__main__':
    solve()