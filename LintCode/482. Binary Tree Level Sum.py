
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def levelSum(self, root, level):
        def dfs(node, depth):
            if not node:
                return 0

            if depth == level:
                return node.val

            l = dfs(node.left, depth + 1)
            r = dfs(node.right, depth + 1)
            return l + r

        return dfs(root, 1)
   



stime = time.time()
print(5 == Solution().levelSum(deserialize('[1,2,3,4,5,6,7,null,null,8,null,null,null,null,9]'), 2))
print('elapse time: {} sec'.format(time.time() - stime))