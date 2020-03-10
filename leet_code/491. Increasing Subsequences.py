
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(start, seq, res):
            if len(seq) >= 2:
                res.add(tuple(seq))
                
            if start == n:
                return
        
            for i in range(start, n):
                if not seq or (seq and seq[-1] <= nums[i]):
                    dfs(i + 1, seq + [nums[i]], res)
            
        n = len(nums)
        res = set()
        dfs(0, [], res)
        return res
   

stime = time.time()
print([[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]] == Solution().findSubsequences([4, 6, 7, 7]))
print('elapse time: {} sec'.format(time.time() - stime))