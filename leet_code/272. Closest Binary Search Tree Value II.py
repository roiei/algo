
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def closestKValues(self, root, target, k):
        def dfs(node):
            if not node:
                return []
            
            res = []
            res += dfs(node.left)
            res += node.val,
            res += dfs(node.right)
            return res
        
        seq = dfs(root)
        diffs = []
        
        for val in seq:
            diffs += (abs(val - target), val),
        
        diffs.sort(key=lambda p: p[0])
        return [v for k, v in diffs[:k]]


stime = time.time()
print([1,2] == Solution().closestKValues(deserialize('[3,1,4,null,2]'), 0.275000, 2))
print('elapse time: {} sec'.format(time.time() - stime))