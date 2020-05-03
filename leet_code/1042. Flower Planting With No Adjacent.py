
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def gardenNoAdj(self, N: int, paths: [[int]]) -> [int]:
        g = collections.defaultdict(list)
        for u, v in paths:
            g[u] += v,
            g[v] += u,
        
        res = [0]*(N + 1)
        nums = collections.defaultdict(int)
        
        for u in range(1, N + 1):
            adjs = []
            for v in g[u]:
                if res[v] != 0:
                    adjs += res[v],

            candidates = {1, 2, 3, 4} - set(adjs)
            res[u] = candidates.pop()

        return res[1:]

    def gardenNoAdj(self, N: int, paths: [[int]]) -> [int]:
        g = collections.defaultdict(list)
        for u, v in paths:
            g[u] += v,
            g[v] += u,
        
        nums = collections.defaultdict(int)
        
        for u in range(1, N + 1):
            adjs = []
            for v in g[u]:
                if nums[v] != 0:
                    adjs += nums[v],

            adjs.sort()
            val = -1
            for i in range(1, 5):
                if i not in adjs:
                    val = i
                    break

            nums[u] = val

        nums = sorted(nums.items(), key=lambda p: p[0])
        nums = [v for k, v in nums]
        return nums
            
        

stime = time.time()
print([1,2,3] == Solution().gardenNoAdj(3, [[1,2],[2,3],[3,1]]))
print([1,2,1,2] == Solution().gardenNoAdj(4, [[1,2],[3,4]]))
print([1,2,3,4] == Solution().gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))
print('elapse time: {} sec'.format(time.time() - stime))