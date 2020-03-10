
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        
        def dfs(node):
            if not node:
                return []
            
            res = [node.val]
            res += dfs(node.left)
            res += dfs(node.right)
            return res
        
        diff = float('inf')
        res = -1
        seq = dfs(root)
        target = int(target + 0.5)

        for val in seq:
            if abs(val - target) < diff:
                diff = abs(val - target)
                res = val
        
        return res


stime = time.time()
print(5 == Solution().closestValue(deserialize('[5,4,9,2,null,8,10]'), target = 6.124780))
print('elapse time: {} sec'.format(time.time() - stime))