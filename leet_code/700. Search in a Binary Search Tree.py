import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            
            if node.val == val:
                return node
        
            ret = dfs(node.left)
            if ret:
                return ret
            
            ret = dfs(node.right)
            return ret
    
        return dfs(root)
    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        q = [root]
        
        while q:
            node = q.pop(0)
            if node.val == val:
                return node
        
            if node.left:
                q += node.left,

            if node.right:
                q += node.right,
            
        return None
        

stime = time.time()
print(tree_is_same(deserialize('[2,1,3]'), Solution().searchBST(deserialize('[4, 2, 7, 1, 3]'), 2)))
print('elapse time: {} sec'.format(time.time() - stime))


