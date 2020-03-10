
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def dfs(node, val):
            if node.val < val:
                if node.right:
                    dfs(node.right, val)
                else:
                    node.right = TreeNode(val)
            else:
                if node.left:
                    dfs(node.left, val)
                else:
                    node.left = TreeNode(val)
            return node
        
        return dfs(root, val)


stime = time.time()
print(Solution().insertIntoBST([4, 2, 7, 1, 3], 5))
print('elapse time: {} sec'.format(time.time() - stime))