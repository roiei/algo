import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, from_left):
            nonlocal tot
            if None == node:
                return
            if None == node.left and None == node.right and True == from_left:
                tot += node.val
            if None != node.left:
                dfs(node.left, True)
            if None != node.right:
                dfs(node.right, False)
        tot = 0
        dfs(root.left, True)
        dfs(root.right, False)
        return tot


stime = time.time()
#print(Solution().sumOfLeftLeaves(deserialize('[3, 9, 20, null, null, 15, 7]')))
print(Solution().sumOfLeftLeaves(deserialize('[1,null,2]')))
print('elapse time: {} sec'.format(time.time() - stime))