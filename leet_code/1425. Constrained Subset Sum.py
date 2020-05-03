
import time
from util.util_list import *
from util.util_tree import *
import bisect
import copy
import collections


class Solution:

    # timeout
    def constrainedSubsetSum(self, nums: [int], k: int) -> int:
        n = len(nums)
        dp = [0]*(n + k)
        
        for i in range(n):
            mx = float('-inf')
            for j in range(i, i + k):
                mx = max(mx, dp[j] + nums[i], nums[i])
                
            dp[i + k] = mx
        
        return max(dp[k:])

    def constrainedSubsetSum(self, nums: [int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        wnd = [0]
        wnd_sorted = [0]
        
        for i in range(n):
            dp[i] = max(nums[i], wnd_sorted[-1] + nums[i])
            wnd += dp[i],
            idx = bisect.bisect_left(wnd_sorted, dp[i])
            wnd_sorted.insert(idx, dp[i])
            
            if len(wnd) > k:
                val = wnd.pop(0)
                wnd_sorted.pop(wnd_sorted.index(val))
        
        return max(dp)
        

stime = time.time()
#print(-1 == Solution().constrainedSubsetSum(nums = [-1,-2,-3], k = 1))
print(16091 == Solution().constrainedSubsetSum([-8269,3217,-4023,-4138,-683,6455,-3621,9242,4015,-3790], 1))
print('elapse time: {} sec'.format(time.time() - stime))