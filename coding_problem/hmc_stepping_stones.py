N = 5
stones = [3, 2, 1, 4, 5]
mx = [float('-inf')]

dp = [1]*N

for i in range(N):
    for j in range(i + 1, N):
        if stones[i] < stones[j]:
            dp[j] = max(dp[i] + 1, dp[j])


print(max(dp))

