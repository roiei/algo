

def catalan(n):
    if n <= 1:
        return 1
    s = 0
    for i in range(n):
        s += catalan(i) * catalan(n-i-1)
    return s


def catalan_dp(n):
    if n <= 1:
        return 1
    dp = [0]*(n+1)
    dp[0] = dp[1] = 1

    for i in range(2, n+1):
        for j in range(i):
            dp[i] = dp[i] + dp[j]*dp[i-j-1]
    return dp[n]


for i in range(10): 
    print(catalan(i))
    print(catalan_dp(i))


# tc = int(input())
# for t in range(tc):
#     n = int(input())
#     res = catalan_dp(n)
#     print(res)