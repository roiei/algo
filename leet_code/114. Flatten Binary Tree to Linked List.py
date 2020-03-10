
import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        def dfs(node, trace):
            trace.append(node.val)
            if None != node.left:
                dfs(node.left, trace)
            if None != node.right:
                dfs(node.right, trace)
        trace = []
        dfs(root, trace)
        trace.pop(0)
        node = root
        while trace:
            node.left = None
            node.right = TreeNode(trace.pop(0))
            node = node.right


stime = time.time()
print(Solution().flatten(deserialize('[1, 2, 5, 3, 4, null, 6]')))
print('elapse time: {} sec'.format(time.time() - stime))