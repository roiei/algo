import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node):
            nonlocal cnt
            cnt += 1
            if None != node.left:
                dfs(node.left)
            if None != node.right:
                dfs(node.right)
        cnt = 0
        dfs(root)
        return cnt


stime = time.time()
print(6 == Solution().countNodes(deserialize('[1,2,3,4,5, 6]')))
print('elapse time: {} sec'.format(time.time() - stime))
