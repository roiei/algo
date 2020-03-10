
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
import heapq


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> [int]:
        def dfs(node):
            res = []
            if not node.left and not node.right:
                return [node.val]

            if node.left:
                res += dfs(node.left)

            if node.right:
                res += dfs(node.right)

            res += [node.val]

            return res

        seq = []
        if root1:
            seq += dfs(root1)
        if root2:
            seq += dfs(root2)

        seq.sort(reverse=False)
        return seq



stime = time.time()
print([0,1,1,2,3,4] == Solution().getAllElements(deserialize('[2,1,4]'), deserialize('[1,0,3]')))
print('elapse time: {} sec'.format(time.time() - stime))