import time
from util.util_list import *


class Solution:
    def get_combs(self, nums, n, k, target, depth, start, trace, res):
        if k == depth:
            if sum(trace) == target:
                res.append(trace[:])
            return
        for i in range(start, n):
            trace.append(nums[i])
            self.get_combs(nums, n, k, target, depth+1, i+1, trace, res)
            trace.pop()

    def combinationSum3(self, k: int, n: int) -> 'List[List[int]]':
        nums = [i for i in range(1, 10)]
        res = []
        self.get_combs(nums, len(nums), k, n, 0, 0, [], res)
        return res


    def combinationSum3(self, k: int, n: int) -> [[int]]:
        
        def dfs(nums, k, start, target, trace, res):
            if k == 0:
                if target == 0:
                    print(trace)
                    res += trace,
                return
            
            for i in range(start, len(nums)):
                if target - nums[i] < 0:
                    return
                dfs(nums, k - 1, i + 1, target - nums[i], trace + [nums[i]], res)
        
        res = []
        dfs([i for i in range(1, 10)], k, 0, n, [], res)
        return res



stime = time.time()
#print(Solution().combinationSum3(3, 7))
print([] == Solution().combinationSum3(2, 18))
print('elapse time: {} sec'.format(time.time() - stime))