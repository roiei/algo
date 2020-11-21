

def get_min_coin_idea(coins, target): # wrong......
    coins.sort()
    print(coins)
    cnt = 0
    for i in range(len(coins)):
        if target < coins[i]:
            break
        cnt += 1

    if cnt > len(coins)-1:
        cnt = len(coins)-1

    num_coin = 0
    while target > 0:
        #print('target = {}, coins[{}] = {}'.format(target, cnt, coins[cnt]))
        while cnt > 0 and target < coins[cnt]:
            cnt -= 1
        #if target < coins[cnt]:
        #    break
        target -= coins[cnt]
        num_coin += 1
    return num_coin


def dfs(coins, depth, left):
    if left == 0:
        return depth    
    res = []
    for coin in coins:
        if left - coin >= 0:
            res += dfs(coins, depth+1, left - coin),
    return min(res) if res else depth


def dfs_mem(coins, depth, left):
    if (depth, left) in mem:
        return[(depth, left)]
    if left == 0:
        return depth    
    res = []
    for coin in coins:
        if left - coin >= 0:
            res += dfs(coins, depth+1, left - coin),
    mem[(depth, left)] = min(res) if res else depth
    return mem[(depth, left)]


def compute_euc(x, y):
   while(y):
       x, y = y, x % y
   return x

def minCoins(coins, m, V): 
    table = [0 for i in range(V + 1)] 
    table[0] = 0
  
    for i in range(1, V + 1): 
        table[i] = sys.maxsize 
  
    for i in range(1, V + 1): 
        for j in range(m): 
            if (coins[j] <= i): 
                sub_res = table[i - coins[j]] 
                if (sub_res != sys.maxsize and 
                    sub_res + 1 < table[i]): 
                    table[i] = sub_res + 1
    return table[V] 


def minCoins(coins, m, V): 
    if (V == 0): 
        return 0
    res = sys.maxsize 
    for i in range(0, m): 
        if (coins[i] <= V): 
            sub_res = minCoins(coins, m, V-coins[i]) 
            if (sub_res != sys.maxsize and sub_res + 1 < res): 
                res = sub_res + 1
    return res


def get_min_coin1(coins, target):
    dp = [float('inf')]*(target+1)
    dp[0] = 0
    mincoin = min(coins)
    for i in range(1, target+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[target]


def get_min_coin(coins, target):
    dp = [float('inf')]*(target+1)
    dp[0] = 0
    mincoin = min(coins)
    for coin in coins:
        for i in range(coin, target+1, coin):
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[target]






mem = {}
coins = [13,96,38,43,17,31,53,85,59,87,22,100,12,24,63,79,36,93,73,14,34,54,3,95,46,15,40,88,58,81,99,51,35,11,41,55,42,97,10,77,48,16,44,76,18,84]
target = 7540  # 79

# [11, 17, 20, 37, 38, 39, 43, 54, 55, 57, 66, 68, 69, 70, 71, 73, 74, 82, 83, 84, 85, 90, 93, 94, 96, 97, 98]
coins = [55,38,85,57,69,90,70,98,20,66,17,43,94,96,68,93,84,74,37,97,11,71,73,39,54,83,82]
target = 7685

# [6, 7, 43, 67, 86]
# coins = [86,7,43,67,6]
# target = 8777  # 103

print(dfs_mem([2, 1], 0, 7))
print(get_min_coin_idea([2, 1], 7))

print(get_min_coin1(coins, target))
print(get_min_coin_idea(coins, target))


# tc = int(input())
# for t in range(tc):
#     target, n = list(map(int, input().split()))
#     coins = list(map(int, input().split()))
#     mem = {}
#     print(dfs_mem(coins, 0, target))