import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        def dfs(node, trace):
            nonlocal res
            trace += node.val,
            if None == node.left and None == node.right:
                res += int(''.join([str(v) for v in trace])),
                trace.pop()
                return
            if None != node.left:
                dfs(node.left, trace)
            if None != node.right:
                dfs(node.right, trace)
            trace.pop()
        dfs(root, [])
        return sum(res)


stime = time.time()
print(Solution().sumNumbers(deserialize('[1,2,3]')))
print('elapse time: {} sec'.format(time.time() - stime))