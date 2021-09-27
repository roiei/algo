
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math


class Node:
    def __init__(self):
        self.idx = -1
        self.value = None
        self.child = []
        
class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        g = collections.defaultdict(lambda: Node())
        res = [0]*len(nums)
        
        for i in range(len(parents)):
            g[i].value = nums[i]
            g[i].idx = i
            
            if -1 == parents[i]:
                continue
                
            g[parents[i]].child += i,

        def dfs(node):
            if not node.child:
                cnt = 1
                while cnt == node.value:
                    cnt += 1
                
                res[node.idx] = cnt
                return [node.value]
            
            vals = [node.value]
            
            for sub in node.child:
                vals += dfs(g[sub])

            vals.sort()

            cnt = 1
            for val in vals:
                if val != cnt:
                    break
                
                cnt += 1

            res[node.idx] = cnt
            return vals
        
        dfs(g[0])
        return res

    def smallestMissingValueSubtree(self, parents, nums):
        n = len(parents)
        res = [1] * n
        seen = [0] * 100010
        if 1 not in nums:
            return res

        children = [[] for i in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        def dfs(i):
            if seen[nums[i]] == 0:
                for j in children[i]:
                    dfs(j)
                seen[nums[i]] = 1

        i = nums.index(1)
        miss = 1

        while i >= 0:
            print(i)
            dfs(i)
            while seen[miss]:
                miss += 1
            res[i] = miss
            i = parents[i]
        return res



stime = time.time()

print([7,1,1,4,2,1] == Solution().smallestMissingValueSubtree(parents = [-1,0,1,0,3,3], nums = [5,4,6,2,1,3]))
#print([1,1,1,1,1,1,1] == Solution().smallestMissingValueSubtree(parents = [-1,2,3,0,2,4,1], nums = [2,3,4,5,6,7,8]))
print('elapse time: {} sec'.format(time.time() - stime))