import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def traverse_level_order(self, root, trace):
        q = []
        q.append([root, 1])
        while q:
            cur = q.pop(0)
            trace.append([cur[0].val, cur[1]])
            if None != cur[0].left:
                q.append([cur[0].left, cur[1]+1])
            if None != cur[0].right:
                q.append([cur[0].right, cur[1]+1])

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        trace = []
        self.traverse_level_order(root, trace)
        trace.sort(key=lambda param:param[1], reverse=True)
        levels = []
        level = []
        pre = trace[0][1]
        while trace:
            t = trace.pop(0)
            if pre != t[1]:
                levels.append(level)
                level = []
                pre = t[1]
            level.append(t[0])
            if not trace:
                levels.append(level)
        return levels

    def do_level_order_from_bottom(self, root: List[TreeNode]) -> List[List[int]]:
        if not root:
            return []

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
            
            q = nq
            lines.insert(0, line)
        
        return lines


stime = time.time()
print(Solution().levelOrderBottom(deserialize('[5, 11, 15, 1, 2, null, 6]')))
#print(Solution().levelOrderBottom(deserialize('[3,9,20,null,null,15,7]')))
print('elapse time: {} sec'.format(time.time() - stime))