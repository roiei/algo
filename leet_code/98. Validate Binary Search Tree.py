import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def check(node, pars):
            if None == node:
                return True
            val = node.val
            if None == val:
                return True
            for v, d in pars:
                if 'L' == d:
                    if val >= v:
                        return False
                elif 'R' == d:
                    if val <= v:
                        return False

            res = [True]
            pars += (val, 'L'),
            res += check(node.left, pars),
            pars.pop()
            pars += (val, 'R'),
            res += check(node.right, pars),
            pars.pop()
            return all(res)
        
        res = [True]
        res += check(root.left, [(root.val, 'L')]),
        res += check(root.right, [(root.val, 'R')]),
        return all(res)

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def dfs(node, l, r):
            if not node:
                return True
        
            if not (l < node.val < r):
                return False
            
            return dfs(node.left, l, min(node.val, r)) and \
                dfs(node.right, max(node.val, l), r)
        
        return dfs(root, float('-inf'), float('inf'))


stime = time.time()
print(Solution().isValidBST(deserialize('[5,1,4,null,null,3,6]')))
print('elapse time: {} sec'.format(time.time() - stime))