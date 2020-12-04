
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution:
    def mostCompetitive(self, nums: [int], k: int) -> [int]:
        def dfs(start, sel):
            if len(sel) == k:
                return sel
            
            mn = [float('inf'), float('inf')]
            for i in range(start, len(nums)):
                res = dfs(i + 1, sel + [nums[i]])
                mn = min(mn, res)
            
            return mn
    
        return dfs(0, [])
    
    def mostCompetitive(self, nums: [int], k: int) -> [int]:
        n = len(nums)
        q = []
        
        for i, num in enumerate(nums):
            heapq.heappush(q, (num, i))

        print(q)
        
        tot, pi = heapq.heappop(q)
        res = [tot]
        k -= 1
        
        while k:
            print(q, k, res)
            cnum, cidx = heapq.heappop(q)
            if pi > cidx:
                continue
            k -= 1
            pi = cidx
            res += cnum,
        
        return res
            
        

stime = time.time()
#print([2,6] == Solution().mostCompetitive([3,5,2,6], k = 2))
print(Solution().mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2], 
3))
print('elapse time: {} sec'.format(time.time() - stime))