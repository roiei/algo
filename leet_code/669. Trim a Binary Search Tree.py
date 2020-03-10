import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            if node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
        
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
    
        return dfs(root)


stime = time.time()
print(Solution().trimBST(deserialize('[1, null, 2]'), 1, 2))
print('elapse time: {} sec'.format(time.time() - stime))