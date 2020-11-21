import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class TreeAncestor:
    def __init__(self, n: int, parent: [int]):
        self.n = n        
        self.parent = parent
        self.mem = {}

    def getKthAncestor(self, node: int, k: int) -> int:
        def dfs(num, val):
            if val == -1 or num == -1:
                return -1

            if (num, val) in self.mem:
                return self.mem[(num, val)]

            ret = num
            if val != 0:
                ret = dfs(self.parent[num], val - 1)

            self.mem[(num, val)] = ret
            return ret
            
        return dfs(node, k)


class TreeAncestor:
    def __init__(self, n, parent):
        self.step = 15
        parent = dict(enumerate(parent))
        self.tbl = [parent]
        
        for s in range(self.step):
            next_parent = collections.defaultdict(lambda: -1)
            for k, v in parent.items():
                if v in parent:
                    next_parent[k] = parent[v]
            self.tbl += next_parent,
            parent = next_parent

    def getKthAncestor(self, node, k):
        step = self.step

        while k > 0 and node != -1:
            while k < (1<<step):
                step -= 1
            
            node = self.tbl[step][node]
            k -= (1<<step)
        
        return node


params = list(zip(["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor"],
[[5,[-1,0,0,1,2]],[3,5],[3,2],[2,2],[0,2],[2,1]], [None,-1,0,-1,-1,0]))


ta = None
for op, param, res in params:
    ret = None
    print(op)
    if op == 'TreeAncestor':
        ta = TreeAncestor(*param)
    elif op == 'getKthAncestor':
        ret = ta.getKthAncestor(param[0], param[1])

    if ret != res:
        print(op, param, ret, res)

