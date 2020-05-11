
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outdegree = collections.defaultdict(int)
        
        for u, v in paths:
            outdegree[u] += 1
            outdegree[v] = outdegree[v]
        
        for k, v in outdegree.items():
            if v == 0:
                return k
        

stime = time.time()
print("Sao Paulo"  == Solution().destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print('elapse time: {} sec'.format(time.time() - stime))