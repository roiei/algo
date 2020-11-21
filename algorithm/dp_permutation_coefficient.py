
# permutation number = n!
#
# nPk = n!/(n-k)!
#


def perm_coeff(n, k):
    dp = [[0]*(k+1) for i in range(n+1)]

    for y in range(n+1):
        for x in range(min(y, k)+1):
            if x == 0:
                dp[y][x] = 1
            else:
                dp[y][x] = x*dp[y-1][x-1] + dp[y-1][x]

            if x < k:
                dp[y][x+1] = 0
    return dp[n][k]


def perm_coeff_n(n, k):
    dp = [1]*(n+1)
    for i in range(1, n+1):
        dp[i] = dp[i-1]*i
    return dp[n]//dp[n-k]


print(perm_coeff(10, 2))
print(perm_coeff_n(10, 2))