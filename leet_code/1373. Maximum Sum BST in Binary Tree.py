
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:

        def dfs(node, mx):
            if not node.left and not node.right:
                mx[0] = max(mx[0], node.val)
                return node.val, True

            lv = rv = 0
            lret = rret = True

            if node.left:
                lv, lret = dfs(node.left, mx)

            if node.right:
                rv, rret = dfs(node.right, mx)

            if not lret or not rret:
                return node.val, False

            if (node.left and node.left.val >= node.val) or \
                (node.right and node.right.val <= node.val):
                return node.val, False

            mx[0] = max(mx[0], lv + rv + node.val)
            return lv + rv + node.val, True

        mx = [0]
        dfs(root, mx)
        return mx[0]

            
stime = time.time()
print(20 == Solution().maxSumBST(deserialize('[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]')))
print(2 == Solution().maxSumBST(deserialize('[4,3,null,1,2]')))
print(0 == Solution().maxSumBST(deserialize('[-4,-2,-5]')))
print(6 == Solution().maxSumBST(deserialize('[2,1,3]')))
print(7 == Solution().maxSumBST(deserialize('[5,4,8,3,null,6,3]')))
print(14 == Solution().maxSumBST(deserialize('[4,8,null,6,1,9,null,-5,4,null,null,null,-3,null,10]')))
print('elapse time: {} sec'.format(time.time() - stime))