import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        def dfs(n, depth, nums, res):
            
            if n == depth:
                if len(nums) > 1 and nums[0] == 0:
                    return
                res += int(''.join(map(str, nums))),
                return
        
            for i in range(10):
                if abs(nums[-1] - i) != K:
                    continue
                
                nums += i,
                dfs(n, depth + 1, nums, res)
                nums.pop()
            
        
        res = []
        nums = []
        for i in range(10):
            nums += i,
            dfs(N - 1, 0, nums, res)
            nums.pop()
        
        return res


stime = time.time()
print(Solution().numsSameConsecDiff(1, 0))
print('elapse time: {} sec'.format(time.time() - stime))