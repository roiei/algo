
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: [[int]]) -> str:
        n = len(s)
        group = [i for i in range(n)]
        
        elems = collections.defaultdict(list)
        
        
        for u, v in pairs:
            if u > v:
                u, v = v, u
            
            if group[v] == v:
                group[v] = group[u]
            elif group[v] != group[u]:
                while group[v] != v:
                    par = group[v]
                    group[v] = group[u]
                    v = par
                group[v] = group[u]
                    
        print(group)
        
        for i in range(n):
            elems[group[i]] += (i, s[i]),
        
        res = [None]*n
        
        print(elems.items())
        
        for k, elem in elems.items():
            idxs = []
            vals = []
            for idx, val in elem:
                idxs += idx,
                vals += val,
            vals.sort()
            
            for idx in idxs:
                res[idx] = vals.pop(0)
            
        return ''.join(res)


stime = time.time()
# print('bacd' == Solution().smallestStringWithSwaps("dcab", [[0,3],[1,2]]))
# print('abcd' == Solution().smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]]))
# print('abc' == Solution().smallestStringWithSwaps("cba", [[0,1],[1,2]]))
print("ffkqttkv" == Solution().smallestStringWithSwaps("fqtvkfkt", [[2,4],[5,7],[1,0],[0,0],[4,7],[0,3],[4,1],[1,3]]))
print('elapse time: {} sec'.format(time.time() - stime))