

def pair(n):
    if n <= 2:
        return n-1
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + (i-1)*dp[i-2]
    return dp[n]



print(pair(3))
print(pair(2))

#print(tile(3))


tc = int(input())
for t in range(tc):
    n = int(input())
    res = pair(n)
    print(res)