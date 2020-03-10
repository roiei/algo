import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        q = [root]
        t = []
        while q:
            cur = q.pop(0)
            t += cur,
            if cur.left:
                q += cur.left,
            if cur.right:
                q += cur.right,
                
        n = len(t)
        limit = 1
        while limit*2 < n:
            limit *= 2
        for i in range(limit):
            if i*2 + 1 < n and t[i].left != t[i*2 + 1]:
                return False
            if i*2 + 2 < n and t[i].right != t[i*2 + 2]:
                return False
        return True

    
stime = time.time()
print(True == Solution().isCompleteTree(deserialize('[1,2,3,4,5,6]')))
print(True == Solution().isCompleteTree(deserialize('[1,2,3,5]')))
print(False == Solution().isCompleteTree(deserialize('[1,2,3,5,null,7,8]')))
print('elapse time: {} sec'.format(time.time() - stime))