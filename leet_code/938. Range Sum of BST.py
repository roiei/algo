import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        q = [root]
        t = []
        while q:
            cur = q.pop(0)
            t += cur.val,
            if cur.left != None:
                q += cur.left,
            if cur.right != None:
                q += cur.right,
        s = 0
        for val in t:
            if L <= val <= R:
                s += val
        return s
            

stime = time.time()
print(Solution().rangeSumBST())
print('elapse time: {} sec'.format(time.time() - stime))