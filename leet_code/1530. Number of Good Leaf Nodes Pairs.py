import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        cnt = 0

        def dfs(node):
            nonlocal cnt

            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            ld = dfs(node.left)
            rd = dfs(node.right)

            for l in ld:
                for r in rd:
                    if l + r <= distance:
                        cnt += 1

            ld = [l + 1 for l in ld if l + 1 < distance]
            rd = [r + 1 for r in rd if r + 1 < distance]
            return ld + rd

        dfs(root)
        return cnt


stime = time.time()
print(2 == Solution().countPairs(deserialize('[1,2,3,4,5,6,7]'), 3))
print(1 == Solution().countPairs(deserialize('[7,1,4,6,null,5,3,null,null,null,null,null,2]'), 3))
print(0 == Solution().countPairs(deserialize('[100]'), 1))
print(1 == Solution().countPairs(deserialize('[1,1,1]'), 2))
print('elapse time: {} sec'.format(time.time() - stime))