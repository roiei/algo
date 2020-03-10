
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def dfs(inorder, postorder):
            if not postorder:
                return None
        
            val = postorder[-1]
            i = 0
            
            while i < len(inorder):
                if inorder[i] == val:
                    break
                i += 1
            
            node = TreeNode(val)
            node.left = dfs(inorder[:i], postorder[:i])
            node.right = dfs(inorder[i + 1:], postorder[i:-1])
            return node
    
        return dfs(inorder, postorder)
            

            
stime = time.time()
print(deserialize('[3,9,20,null,null,15,7]') == Solution().buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]))
print('elapse time: {} sec'.format(time.time() - stime))