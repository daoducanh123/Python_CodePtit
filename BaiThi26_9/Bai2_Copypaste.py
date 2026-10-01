import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    idx = 1
    for _ in range (T):
        n = int(input_data[idx])
        x = int(input_data[idx+1])
        y = int(input_data[idx+2])
        z = int(input_data[idx+3])
        idx+=4
        
        dp=[0] *(n+2)
        dp[1] = x
        
        for i in range(2,n+1):
            if i % 2 ==0:
                dp[i] = min(dp[i-1]+x, dp[i//2] + z)
            else:
                dp[i] = min(dp[i-1]+x, dp[(i+1) // 2] +z + y)
        print(dp[n])
        
if __name__ == '__main__':
    solve()