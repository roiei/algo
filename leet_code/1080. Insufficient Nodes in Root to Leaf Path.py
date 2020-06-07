
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node, tot):
            tot += node.val
            
            if not node.left and not node.right:
                if tot < limit:
                    return None
                return node
            
            if node.left:
                node.left = dfs(node.left, tot)
            
            if node.right:
                node.right = dfs(node.right, tot)
            
            if not node.left and not node.right:
                return None
            return node
        
        root = dfs(root, 0)
        return root
                
                

stime = time.time()
print(traverse_level(deserialize('[1,2,3,4,null,null,7,8,9,null,14]')) == traverse_level(Solution().sufficientSubset(deserialize('[1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]'), 1)))
print('elapse time: {} sec'.format(time.time() - stime))

