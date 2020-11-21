
mod = 10**9 + 7

def comb(n, r):
    if n == r or r == 0:
        return 1

    dp = [0]*(r+1)
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(min(i, r), 0, -1):
            dp[j] = (dp[j] + dp[j-1]) % mod
    return dp[r]


mem = {}
def comb_2(n, r):
    if (n, r) in mem:
        return mem[(n, r)]
    if n == r or r == 0:
        return 1
    mem[(n, r)] = comb_2(n-1, r-1) + comb_2(n-1, r)
    return mem[(n, r)]


print(comb(778, 116))
print()
print(comb_2(778, 116)%mod)

# tc = int(input())
# for t in range(tc):
#     n, r = map(int, input().split())
#     mod = 10**9 + 7
#     print(comb(n, r)%mod)