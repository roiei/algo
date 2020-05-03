
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            res = []
            if not node.left and not node.right:
                return [node.val]

            if node.left:
                res += dfs(node.left)
            res += node.val,
            if node.right:
                res += dfs(node.right)
            return res

        res = sorted(dfs(root))

        def do(l, r):
            if l > r:
                return None

            m = (l + r)//2
            node = TreeNode(res[m])
            node.left = do(l, m - 1)
            node.right = do(m + 1, r)
            return node

        btree = do(0, len(res) - 1)

        return btree





stime = time.time()
print(Solution().balanceBST(deserialize('[1,null,2,null,3,null,4,null,null]')))
print('elapse time: {} sec'.format(time.time() - stime))