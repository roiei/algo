
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q = [(1, root)]
        levels = collections.defaultdict(int)
        
        while q:
            nq = []
            
            while q:
                lev, node = q.pop(0)
                levels[lev] += node.val
                
                if node.left:
                    nq += (lev + 1, node.left),
                
                if node.right:
                    nq += (lev + 1, node.right),
            
            q = nq
        
        levels = sorted(levels.items(), key=lambda p: p[1], reverse=True)
        return levels[0][0]
        

stime = time.time()
print(2 == Solution().maxLevelSum(deserialize('[1,7,0,7,-8,null,null]')))
print('elapse time: {} sec'.format(time.time() - stime))