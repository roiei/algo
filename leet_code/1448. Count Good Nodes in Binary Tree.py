
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def dfs(node, seq):
            nonlocal cnt

            if not node:
                return

            if not seq or (seq and seq[-1] <= node.val):
                cnt += 1

            idx = bisect.bisect_left(seq, node.val)
            seq.insert(idx, node.val)

            dfs(node.left, seq[::])
            dfs(node.right, seq[::])

        dfs(root, [])
        return cnt


stime = time.time()
print(4 == Solution().goodNodes(deserialize('[3,1,4,3,null,1,5]')))
print('elapse time: {} sec'.format(time.time() - stime))