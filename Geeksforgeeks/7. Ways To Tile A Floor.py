

def tile(n):
    if n <= 3:
        return n

    dp = [1]*(n+1)
    dp[1] = 2
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]


#print(tile(5))
#print(tile(3))


tc = int(input())
for t in range(tc):
    n = int(input())
    res = tile(n)
    print(res)