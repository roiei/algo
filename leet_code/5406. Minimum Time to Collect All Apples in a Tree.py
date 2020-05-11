
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def minTime(self, n: int, edges: [[int]], hasApple: [bool]) -> int:
        def dfs(u):
            visited.add(u)
            res = 0

            for v in g[u]:
                if v in visited:
                    continue
                
                res += dfs(v)

            if (hasApple[u] or (not hasApple[u] and res)) and u != 0:
                res += 2
            
            return res
    
        g = collections.defaultdict(list)
        
        for u, v in edges:
            g[u] += v,
            g[v] += u,
        
        visited = set()
        res = dfs(0)
        return res

                

stime = time.time()
print(8 == Solution().minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]))
print(6 == Solution().minTime(4, [[0,1],[1,2],[0,3]], [True,True,True,True]))
print('elapse time: {} sec'.format(time.time() - stime))