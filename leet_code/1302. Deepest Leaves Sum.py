
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = [root]
        lines = []
        
        while q:
            nq = []
            line = []
            
            while q:
                node = q.pop(0)
                line += node.val,
                if node.left:
                    nq += node.left,
                if node.right:
                    nq += node.right,
            
            lines += line,
            q = nq
        
        return sum(val for val in lines[-1])
            


stime = time.time()
print(15 == Solution().deepestLeavesSum(deserialize("[1,2,3,4,5,null,6,7,null,null,null,null,8]")))
print('elapse time: {} sec'.format(time.time() - stime))