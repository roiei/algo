
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        def dfs(node):
            nonlocal mx
            if not node.left and not node.right:
                return 0, 1, 0  # left, mine, right

            llen = rlen = 0
            if node.left:
                cl, c, cr = dfs(node.left)
                llen = c + cr

            if node.right:
                cl, c, cr = dfs(node.right)
                rlen = c + cl

            mx = max(mx, llen + 1, rlen + 1)
            return llen, 1, rlen

        mx = 0
        ret = dfs(root)
        return mx - 1 if mx else 0
            
            
stime = time.time()
print(3 == Solution().longestZigZag(deserialize('[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]')))
print(4 == Solution().longestZigZag(deserialize('[1,1,1,null,1,null,null,1,1,null,1]')))
print(0 == Solution().longestZigZag(deserialize('[1]')))
print('elapse time: {} sec'.format(time.time() - stime))