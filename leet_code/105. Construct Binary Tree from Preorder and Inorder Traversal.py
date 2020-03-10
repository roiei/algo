
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def dfs(preorder, inorder):
            if not preorder:
                return None
            
            val = preorder[0]
            
            i = 0
            left_pre = []
            left_in = []
            while i < len(inorder) and inorder[i] != val:
                left_pre += preorder[i + 1],
                left_in += inorder[i],
                i += 1
            
            node = TreeNode(val)
            node.left = dfs(left_pre, left_in)
            node.right = dfs(preorder[i + 1:], inorder[i + 1:])
            return node
    
        return dfs(preorder, inorder)

            
stime = time.time()
print(deserialize('[3,9,20,null,null,15,7]') == Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))
print('elapse time: {} sec'.format(time.time() - stime))