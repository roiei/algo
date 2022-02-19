import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for u, v in roads:
            g[u] += v,
            g[v] += u,
        
        most = sorted(g.items(), key=lambda p: len(p[1]), reverse=True)
        most_freqs = [k for k, v in most if len(v) == len(most[0][1])]
        mx = 0
        
        for u in most_freqs:
            num_u = len(g[u])
            
            for node in range(n):
                if node == u:
                    continue
                
                neis = len(g[node])
                if u in g[node]:
                    neis -= 1
                
                mx = max(mx, num_u + neis)
        
        return mx

    def get_max_rank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0

        g = collections.defaultdict(list)
        for u, v in roads:
            g[u] += v,
            g[v] += u,
        
        most = sorted(g.items(), key=lambda p: len(p[1]), reverse=True)
        mx = 0
        i = 0

        while i < len(most) and len(most[i][1]) == len(most[0][1]):
            u = most[i][0]
            num_u = len(g[u])
            
            for v in range(n):
                if v == u:
                    continue
                
                neis = len(g[v])
                if u in g[v]:
                    neis -= 1
                
                mx = max(mx, num_u + neis)

            i += 1

        return mx
        

stime = time.time()
print(5 == Solution().maximalNetworkRank(n=5, roads=[[0,2],[2,1],[2,3],[1,4],[1,5]]))
# print(4 == Solution().maximalNetworkRank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]))
# print(5 == Solution().maximalNetworkRank(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))
print('elapse time: {} sec'.format(time.time() - stime))
