
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
from typing import List


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node, depth, sub):
            nonlocal mx
            depth += 1
            
            if not node.left and not node.right:
                if mx < depth:
                    mx = depth
                    sub[0] = node
                return depth
        
            ld = rd = 0
            if node.left:
                ld = dfs(node.left, depth, sub)
            
            if node.right:
                rd = dfs(node.right, depth, sub)
            
            if ld == rd and mx <= ld:
                mx = ld
                sub[0] = node
            
            return max(ld, rd)
            
    
        mx = 0
        sub = [None]
        dfs(root, 0, sub)
        return sub[0]

            
stime = time.time()
print(tree_is_same(deserialize('[2,7,4]'), Solution().lcaDeepestLeaves(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'))))
print(tree_is_same(deserialize('[0,3,1,4,null,2,null,null,6,null,5]'), Solution().lcaDeepestLeaves(deserialize('[0,3,1,4,null,2,null,null,6,null,5]'))))
print('elapse time: {} sec'.format(time.time() - stime))