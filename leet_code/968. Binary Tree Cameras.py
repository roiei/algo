
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.cnt = 0
        
        # 0: not covered
        # 1: caemra
        # 2: covered but no camera
        
        def dfs(node):
            if not node.left and not node.right:
                return 0    # leaf

            l = r = -1
            if node.left:
                l = dfs(node.left)
                
            if node.right:
                r = dfs(node.right)
            
            if l == 0 or r == 0:
                self.cnt += 1
                return 1
            
            if l == 1 or r == 1:
                return 2
            
            return 0
    
        res = dfs(root)
        return self.cnt + (1 if res == 0 else 0)
            
            
stime = time.time()
print(1 == Solution().minCameraCover(deserialize('[0,0,null,0,0]')))
print(2 == Solution().minCameraCover(deserialize('[0,0,null,0,null,0,null,null,0]')))
print(2 == Solution().minCameraCover(deserialize('[0,0,null,null,0,0,null,null,0,0]')))
print('elapse time: {} sec'.format(time.time() - stime))