class Solution(object):
    def check_coin(self, coins, amount, acc, depth):
        if acc > amount:
            return -1
        if acc == amount:
            return depth
        res = []
        for i in coins:
            res.append(self.check_coin(coins, amount, acc + i, depth+1))
        ret = [i for i in res if i > 0]
        if ret:
            return min(ret)
        else:
            return -1

    def coinChange_es(self, coins: 'List[int]', amount: 'int') -> 'int':
        if 0 == amount:
            return 0
        res = []
        for i in coins:
            res.append(self.check_coin(coins, amount, i, 1))
        ret = [i for i in res if i > 0]
        if ret:
            return min(ret)
        else:
            return -1

    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        INF = 0x7ffffffe
        coin_count = [0] + [INF] * amount   # 0 coin -> can be 0 coin with 0 coin
        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    # dp[i] is previous coin
                    # dp[i] + 1 => prev coin + cur coin
                    coin_count[i+coin] = min(coin_count[i+coin], coin_count[i] + 1)
        return coin_count[amount] if coin_count[amount] != INF else -1

    def coinChange(self, coins, amount):
        if not coins:
            return -1
        if 0 == amount:
            return 0
        dp = [float('inf')]*(amount+1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(amount+1):
            for coin in coins:
                if i+coin > amount:
                    continue
                dp[i+coin] = min(dp[i+coin], dp[i]+1)
        return dp[-1] if dp[-1] != float('inf') else -1

    def coinChange(self, coins, amount):
        if not coins:
            return -1
        
        def dfs(coins, tot, depth):
            nonlocal mem
            if (tot, depth) in mem:
                return mem[(tot, depth)]
            if tot > amount:
                return -1
            if tot == amount:
                return depth

            res = []
            for coin in coins:
                ret = dfs(coins, tot+coin, depth+1)
                if -1 != ret:
                    res += ret,
            mem[(tot, depth)] = -1 if not res else min(res)
            return mem[(tot, depth)]

        mem = {}
        res = dfs(coins, 0, 0)
        print(res)
        return res


    def coinChange(self, coins, amount):
        if not coins or 0 == amount:
            return 0
        dp = [float('inf')]*(amount + 1)
        
        for coin in coins:
            if coin > amount:
                continue
            dp[coin] = 1
            for i in range(coin+1, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if float('inf') != dp[-1] else -1




#print(Solution().coinChange([1, 2, 5], 100))
print(3 == Solution().coinChange([1, 2, 5], 11))
#print(-1 == Solution().coinChange([2], 3))
#print(Solution().coinChange([2], 1))
#print(Solution().coinChange([1], 0))

