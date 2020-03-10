import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        if not root:
            return []
        q = [root]
        ts = []
        while q:
            nq = []
            t = []
            while q:
                cur = q.pop(0)
                t += cur.val,
                if None != cur.left:
                    nq += cur.left,
                if None != cur.right:
                    nq += cur.right,
            q = nq
            ts += t,
        res = []
        for t in ts:
            res += t[-1],
        return res


stime = time.time()
print([1, 3, 4] == Solution().rightSideView([1,2,3,null,5,null,4]))
print('elapse time: {} sec'.format(time.time() - stime))