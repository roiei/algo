import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = [root]
        ts = []
        while q:
            nq = []
            t = []
            while q:
                cur = q.pop(0)
                t += cur,
                if cur.left:
                    nq += cur.left,
                if cur.right:
                    nq += cur.right,
            q = nq
            ts += t,
        for t in ts:
            if not t:
                continue
            t[-1].next = None
            for i in range(len(t)-1, 0, -1):
                t[i-1].next = t[i]
        
        return root

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = [root]
        levels = []
        
        while q:
            nq = []
            nodes = []
            
            while q:
                node = q.pop(0)
                nodes += node,
                if node.left:
                    nq += node.left,
                if node.right:
                    nq += node.right,
                
            levels += nodes,
            q = nq
        
        for nodes in levels:
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            nodes[-1].next = None
        
        return root
            

stime = time.time()
print(Solution().verticalTraversal(deserialize('[3,9,20,null,null,15,7]')))
print('elapse time: {} sec'.format(time.time() - stime))