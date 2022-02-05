import collections


W, N = 100, 2   # capacity, num items
items = [
    [90, 1],    # weight, value
    [70, 2]
]


weights = []
values = []

for w, v in items:
    weights += w,
    values += w*v,


# 100 3
# 150 2
# 200 3
# -> create
# 1    2    3    <-- reduce the number of items from 10^6 to 10^4
#     150  300


weight_sums = collections.defaultdict(int)
for w, v in items:
    weight_sums[v] += w

weight_sums = sorted(weight_sums.items(), key=lambda p: p[0], reverse=True)
tot = 0

for v, w in weight_sums:
    if W >= w:
        W -= w
        tot += v*w
    else:
        tot += v*W
        W = 0
        break

print(tot)


def knapsack(weights, values, N, K):
    """
        N: number of items
        K: capacity
        weights: items' weight
        values: items' value
    """
    dp = [[0]*(K + 1) for _ in range(N + 1)]

    for i in range(N):
        weight = weights[i]
        value = values[i]

        for j in range(K):
            if weight <= j + 1:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i][j - weight + 1] + value)
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]

    return dp[N][K]


def knapsack(weights, values, N, K):
    """
        N: number of items
        K: capacity
        weights: items' weight
        values: items' value
    """
    dp = [[[0]*2 for j in range(K + 1)] for _ in range(N + 1)] # [value, weight]

    for i in range(N):
        weight = weights[i]
        value = values[i]

        for j in range(K):
            if weight <= j + 1:
                if dp[i][j + 1][0] > dp[i][j - weight + 1][0] + value:
                    dp[i + 1][j + 1][0] = dp[i][j + 1][0]
                    dp[i + 1][j + 1][1] = dp[i][j + 1][1]
                else:
                    dp[i + 1][j + 1][0] = dp[i][j - weight + 1][0] + value
                    dp[i + 1][j + 1][1] = dp[i][j - weight + 1][1] + weight
            else:
                dp[i + 1][j + 1][0] = dp[i][j + 1][0]

    return dp[N][K]


# it is not a knapsack problem !
# very easy problem


# value, used_weight = knapsack(weights, values, N, W)
# tot_weight = value + (W - used_weight)
# print(tot_weight)
