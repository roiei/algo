import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        num = 0
        def dfs(node, target):
            nonlocal num
            if not node:
                return
            if target - node.val == 0:
                num += 1
            dfs(node.left, target - node.val) 
            dfs(node.right, target - node.val)
        q = [root]
        while q:
            cur = q.pop(0)
            dfs(cur, target)
            if None != cur.left:
                q += cur.left,
            if None != cur.right:
                q += cur.right,
        return num

    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        num = 0

        def dfs(node, target, inc):
            nonlocal num
            if not node:
                return
            inc += node.val
            if target == inc:
                num += 1
            dfs(node.left, target, inc)
            dfs(node.right, target, inc)
            inc -= node.val

        q = [root]
        while q:
            cur = q.pop(0)
            dfs(cur, target, 0)
            if None != cur.left:
                q += cur.left,
            if None != cur.right:
                q += cur.right,
        return num

stime = time.time()
#print(Solution().pathSum(deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]'), 22))
#print(Solution().pathSum(deserialize('[1]'), 0))
#print(Solution().pathSum(deserialize('[-2,null,-3]'), -5))
print(Solution().pathSum(deserialize('[6,5,null,1,null,2,5,null,null,6,12]'), 12))
print('elapse time: {} sec'.format(time.time() - stime))