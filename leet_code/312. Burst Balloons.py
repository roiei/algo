import time
from functools import lru_cache


class Solution:
    cache = {}
    def get_max(self, nums, n, depth):
        key = ':'.join([str(i) for i in nums])
        if key in self.cache:
            return self.cache[key]
        if not nums:
            return 0
        res = []
        for i in range(n):
            left = right = 1
            if i > 0:
                left = nums[i-1]
            if i < n-1:
                right = nums[i+1]
            coin = left*nums[i]*right

            n_nums = nums[:i] + nums[i+1:]
            res.append(coin + self.get_max(n_nums, len(n_nums), depth+1))
        
        self.cache[key] = max(res)
        return max(res)

    def maxCoins_es(self, nums: 'List[int]') -> int:
        self.cache = {}
        n = len(nums)
        coin = self.get_max(nums, n, 0)
        return coin

    def maxCoins(self, nums: 'List[int]') -> int:
        if not nums:
            return 0

        nums.insert(0, 1)
        nums.append(1)
        total = 0

        print(nums)

        while len(nums) > 2:
            mcoin = 0
            idx = -1
            for i in range(1, len(nums)-1):
                coin = nums[i-1]*nums[i]*nums[i+1]
                if mcoin < coin:
                    mcoin = coin
                    idx = i
            print(mcoin)
            total += mcoin
            nums.pop(idx+1)
        return total


    def maxCoins(self, nums: [int]) -> int:
        #@lru_cache(None)

        def max_coins(i, j, l, r):
            if (l, r) in mem:
                return mem[(l, r)]
            if i > j:
                return 0
            coins = 0
            for k in range(i, j+1):
                cur = l*nums[k]*r
                left = max_coins(i, k-1, l, nums[k])
                right = max_coins(k+1, j, nums[k], r)
                coins = max(coins, cur + left + right)

                #print(' i = {:3}, j = {:3}, k = {:3}, cur = {:3}, left = {:3}, right = {:3}, coins = {:3}'.format(i, j, k, cur, left, right, cur+left+right))
            mem[(l, r)] = coins
            return coins
        
        mem = {}
        return max_coins(0, len(nums)-1, 1, 1)


    def maxCoins(self, nums: [int]) -> int:
        def dfs(l, r, lval, rval):
            if l > r:
                return 0
            coins = 0
            for i in range(l, r+1):
                lret = dfs(l, i-1, lval, nums[i])
                rret = dfs(i+1, r, nums[i], rval)
                coins = max(coins, lval*nums[i]*rval + lret + rret)
            return coins

        return dfs(0, len(nums)-1, 1, 1)

    def maxCoins(self, nums: [int]) -> int:
        
        def dfs(nums):
            if not nums:
                return 0
        
            mcoin = 0
            mx = 0
            
            for i in range(len(nums)):
                lv = rv = 1
                
                if i > 0:
                    lv = nums[i - 1]
                if i < len(nums) - 1:
                    rv = nums[i + 1]
                
                val = lv*nums[i]*rv
                
                mx = max(mx, val + dfs(nums[:i] + nums[i + 1:]))

            return mx
        
        return dfs(nums)







#nums = [35,16,83,87,84,59,48,41,20,54]

stime = time.time()
print(167 == Solution().maxCoins([3,1,5,8]))
#print(3446 == Solution().maxCoins([8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2,2]))
print('elapse time: {} sec'.format(time.time() - stime))
