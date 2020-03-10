import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        def dfs(node, target, trace):
            trace += node.val,
            if None == node.left and None == node.right:
                if target == sum(trace):
                    trace.pop()
                    return True
                trace.pop()
                return False
            res = []
            if None != node.left:
                res += dfs(node.left, target, trace),
            if None != node.right:
                res += dfs(node.right, target, trace),
            trace.pop()
            return any(res)
        ret = dfs(root, target, [])
        return ret


stime = time.time()
print(Solution().distanceK(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), 5, 2))
print('elapse time: {} sec'.format(time.time() - stime))