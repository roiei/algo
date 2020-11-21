import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    """
    @param nums: a list of integers
    @return: return an integer
    """
    def pathSum(self, nums):
        
        vals = {}
        
        for num in nums:
            num = str(num)
            y = int(num[0])
            x = int(num[1])
            val = int(num[2])
            vals[(y, x)] = val
        
        def dfs(vals, y, x):
            if (y, x) not in vals:
                return None
            
            node = TreeNode(vals[(y, x)])
            node.left = dfs(vals, y + 1, x)
            node.right = dfs(vals, y + 1, x + 1)
            return node
        
        root = dfs(vals, 1, 1)
        
        def path(node, inc, res):
            if not node.left and not node.right:
                res[0] += inc + node.val
                return
            if node.left:
                path(node.left, inc + node.val, res)
            if node.right:
                path(node.right, inc + node.val, res)
        
        res = [0]
        path(root, 0, res)
        return res[0]


stime = time.time()
print(43 == Solution().pathSum([115,213,227,336,345]))
print('elapse time: {} sec'.format(time.time() - stime))