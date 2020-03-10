

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        if not root:
            return []
        q = [root]
        trace = []
        while q:
            nq = []
            t = []
            while q:
                cur = q.pop(0)
                t.append(cur.val)
                for child in cur.children:
                    nq.append(child)
            trace.append(t)
            q = nq
        return trace

