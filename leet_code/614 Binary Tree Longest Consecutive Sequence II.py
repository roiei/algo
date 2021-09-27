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
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        def dfs(node):
            if not node:
                return 0, 0, 0

            lmx, lpn, lnn = dfs(node.left)
            rmx, rpn, rnn = dfs(node.right)

            if node.left and node.left.val + 1 == node.val:
                lpn += 1

            if node.left and node.left.val - 1 == node.val:
                lnn += 1

            if node.right and node.right.val + 1 == node.val:
                rpn += 1

            if node.right and node.right.val - 1 == node.val:
                rnn += 1

            return max(lmx, rmx, lpn + rnn, lnn + rpn), \
                max(lpn, rpn), max(lnn, rnn)

        mx, pn, pn = dfs(root)
        print(mx)
        return mx

            
            

stime = time.time()
print(4 == Solution().longestConsecutive2(deserialize('[1,2,0,3]')))
print(2 == Solution().longestConsecutive2(deserialize('[1,2,-5,4,None,5,6]')))
print(3 == Solution().longestConsecutive2(deserialize('[1,None,2,None,4,None,5,None,6]')))
print('elapse time: {} sec'.format(time.time() - stime))
