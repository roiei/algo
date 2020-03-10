import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def zigzagLevelOrder_1(self, root: TreeNode) -> 'List[List[int]]':
        if not root:
            return []
        q = [root]
        trace = []
        while q:
            nq = []
            t = []
            while q:
                cur = q.pop(0)
                t.append(cur.val)
                if None != cur.left:
                    nq.append(cur.left)
                if None != cur.right:
                    nq.append(cur.right)
            q = nq
            trace.append(t)
        cnt = 0
        for i in range(len(trace)):
            if 0 != cnt%2:
                trace[i] = list(reversed(trace[i]))
            cnt += 1
        return trace

    def zigzagLevelOrder(self, root: TreeNode) -> 'List[List[int]]':
        if not root:
            return []
        q = [root]
        trace = []
        toggle = False
        while q:
            nq = []
            t = []
            while q:
                cur = q.pop()
                if False == toggle:
                    if None != cur.left:
                        nq.append(cur.left)
                    if None != cur.right:
                        nq.append(cur.right)
                else:
                    if None != cur.right:
                        nq.append(cur.right)
                    if None != cur.left:
                        nq.append(cur.left)
                t.append(cur.val)
            q = nq
            trace.append(t)
            toggle = True if False == toggle else False
        return trace


stime = time.time()
print(Solution().zigzagLevelOrder(deserialize('[1,2,3,4,null,null,5]')))
print('elapse time: {} sec'.format(time.time() - stime))
