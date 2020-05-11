
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        nodes = collections.defaultdict(None)
        tot = 0
        
        def dfs(nodes, node, pos):
            nonlocal tot
            
            if not node:
                return
            
            nodes[node.val] = node
            tot += node.val
            
            dfs(nodes, node.left, pos - 1)
            dfs(nodes, node.right, pos + 1)
        
        dfs(nodes, root, 0)
        
        nodes = sorted(nodes.items(), key=lambda p: p[0])

        preval = 0
        for val, node in nodes:
            tot -= preval
            node.val, preval = tot, node.val
        
        return root
        

stime = time.time()
print(traverse_level(deserialize('[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]')) == traverse_level(Solution().bstToGst(deserialize('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'))))
print('elapse time: {} sec'.format(time.time() - stime))