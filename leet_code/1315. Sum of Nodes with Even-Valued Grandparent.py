
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def dfs(node, grand, parent):
            if not node:
                return 0
            
            res = 0
            if grand == True:
                res += node.val
            
            res += dfs(node.left, parent, node.val%2 == 0)
            res += dfs(node.right, parent, node.val%2 == 0)
            return res
    
        return dfs(root, False, False)
            


stime = time.time()
print(18 == Solution().sumEvenGrandparent(deserialize('[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]')))
print('elapse time: {} sec'.format(time.time() - stime))