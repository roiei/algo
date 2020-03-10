import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def dfs(node, depth, v, d):
            if not node:
                return None
            if depth == d-1:
                nl = node.left
                nr = node.right
                node.left = TreeNode(v)
                node.right = TreeNode(v)
                node.left.left = nl
                node.right.right = nr
            else:
                node.left = dfs(node.left, depth+1, v, d)
                node.right = dfs(node.right, depth+1, v, d)
            return node
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        return dfs(root, 1, v, d)

    
stime = time.time()
print(Solution().addOneRow(deserialize('[4,2,6,3,1,5,null]'), 1, 2))
print('elapse time: {} sec'.format(time.time() - stime))