import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        def dfs(node1, node2):
            if not node1 or not node2:
                return node1 if node1 else node2
                
            node = TreeNode(node1.val + node2.val)
            node.left = dfs(node1.left, node2.left)
            node.right = dfs(node1.right, node2.right)
            return node
    
        node = dfs(t1, t2)
        return node


stime = time.time()
print(2 == Solution().mergeTrees(8))
print('elapse time: {} sec'.format(time.time() - stime))
