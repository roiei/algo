
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        
        tot = 0
        q = [root]
        while q:
            node = q.pop(0)
            tot += node.val
            if node.left:
                q += node.left,
            if node.right:
                q += node.right,

        def do(node):
            if not node.left and not node.right:
                return node.val, 0 # sum, max
        
            ls = lm = rs = rm = 0
            
            if node.left:
                ls, lm = do(node.left)
            
            if node.right:
                rs, rm = do(node.right)
            
            mx = max((tot - ls)*ls, (tot - rs)*rs)
            
            return node.val + ls + rs, max(mx, rm, lm)

    
        s, m = do(root)
        m = m%(10**9 + 7)
        return m

            
stime = time.time()
print(90 == Solution().maxProduct(deserialize('[1,null,2,3,4,null,null,5,6]')))
print('elapse time: {} sec'.format(time.time() - stime))