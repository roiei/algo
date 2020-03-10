import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        def dfs(node, trace):
            if None == node:
                return
            if None == node.left and None == node.right:
                trace += str(node.val),
                return
            trace += str(node.val),
            trace += '(',
            dfs(node.left, trace)
            trace += ')',
            if None != node.right:
                trace += '(',
                dfs(node.right, trace)
                trace += ')',
        trace = []
        dfs(t, trace)
        return ''.join(trace)


stime = time.time()
print(Solution().tree2str(deserialize('[1,2,3,4]')))
print('elapse time: {} sec'.format(time.time() - stime))