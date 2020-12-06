import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            if n%i == 0:
                print(i)
                cnt += 1

            if cnt == k:
                return i

        return -1

    def kthFactor(self, n: int, k: int) -> int:
        def dfs(n, nums, seq):
            if n == 1:
                nums |= set([1] + seq)
                return
            
            divisors = {2, 3, 4, 5, 7}
            if 1 != n:
                divisors.add(n)
        
            for divisor in list(divisors):
                if 0 == n%divisor:
                    dfs(n//divisor, nums, seq + [divisor])
        
        nums = set()
        dfs(n, nums, [])
        nums = sorted(nums)
        print(nums)
        if len(nums) < k:
            return -1
        
        print(nums)
        return nums[k - 1]


stime = time.time()
#print(3 == Solution().kthFactor(n = 12, k = 3)) # [1, 2, 3, 4, 6, 12]
#print(7 == Solution().kthFactor(n = 7, k = 2))
#print(-1 == Solution().kthFactor(n = 4, k = 4))
#print(23 == Solution().kthFactor(n = 23, k = 2))
#print(3 == Solution().kthFactor(n = 39, k = 2))
print(Solution().kthFactor(n = 114, k = 8))
print('elapse time: {} sec'.format(time.time() - stime))

