import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect
from typing import List


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def traverse(node, depth):
            if None == node.left and None == node.right:
                return depth, True
            ldepth = rdepth = depth
            lbalanced = rbalanced = True
            if None != node.left:
                ldepth, lbalanced = traverse(node.left, depth+1)
            if None != node.right:
                rdepth, rbalanced = traverse(node.right, depth+1)
            balanced = [lbalanced, rbalanced, False if 1 < abs(ldepth-rdepth) else True]
            return max(ldepth, rdepth), all(balanced)
        depth, balanced = traverse(root, 1)
        return balanced

    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node, depth):
            if not node:
                return True, depth

            lr, ld = dfs(node.left, depth + 1)
            rr, rd = dfs(node.right, depth + 1)
            if not lr or not rr:
                return False, max(ld, rd)

            diff = abs(ld - rd)
            if 1 < diff:
                return False, max(ld, rd)

            return True, max(ld, rd)

        ret, res = dfs(root, 0)
        return ret or res <= 1


stime = time.time()
print(False == Solution().isBalanced(deserialize('[1,2,2,3,3,null,null,4,4]')))
#print(False == Solution().isBalanced(deserialize('[1,2,2,3,null,null,3,4,null,null,4]')))
print('elapse time: {} sec'.format(time.time() - stime))
