import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []
        def dfs(node, trace, res, target):
            trace += node.val,
            if None == node.left and None == node.right:
                if target == sum(trace):
                    res += trace[:],
                trace.pop()
                return
            if None != node.left:
                dfs(node.left, trace, res, target)
            if None != node.right:
                dfs(node.right, trace, res, target)
            trace.pop()
        res = []
        dfs(root, [], res, target)
        return res


stime = time.time()
print(Solution().distanceK(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), 5, 2))
print('elapse time: {} sec'.format(time.time() - stime))