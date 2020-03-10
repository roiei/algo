import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node.left and not node.right:
                return True if node.val == 0 else False

            ret_l = ret_r = False
            if node.left:
                ret_l = dfs(node.left)
            if node.right:
                ret_r = dfs(node.right)

            if ret_l:
                node.left = None
            if ret_r:
                node.right = None
            return True if (not node.left and not node.right \
                and node.val == 0) else False
        dfs(root)
        return root
        
            

stime = time.time()
#print(traverse_level(Solution().pruneTree(deserialize('[1,null,0,0,1]'))))
print(traverse_level(Solution().pruneTree(deserialize('[1,0,1,0,0,0,1]'))))
print('elapse time: {} sec'.format(time.time() - stime))