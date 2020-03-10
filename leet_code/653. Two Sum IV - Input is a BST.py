import time
from util_tree import *


class Solution:
    def trace(self, node):
        t = []
        q = [node]
        while q:
            cur = q.pop(0)
            t.append(cur.val)
            if None != cur.left:
                q.append(cur.left)
            if None != cur.right:
                q.append(cur.right)
        return t

    def findTarget(self, root: TreeNode, k: int) -> bool:
        t = self.trace(root)
        t.sort()
        n = len(t)
        if 0 == n or 1 == n:
            return False
        l = 0
        r = n-1
        while l < r:
            s = t[l]+t[r]
            if k == s:
                return True
            if s > k:
                r -= 1
            else:
                l += 1
        return True if s == k else False


stime = time.time()
print(Solution().findTarget(deserialize('[5, 3, 6, 2, 5, null, 7]'), 9))
print(Solution().findTarget(deserialize('[2, 1, 3]'), 3))
print(Solution().findTarget(deserialize('[5,3,6,2,4,null,7]'), 28))
print(Solution().findTarget(deserialize('[1]'), 2))
print(Solution().findTarget(deserialize('[2,null,3]'), 6))
print('elapse time: {} sec'.format(time.time() - stime))

