
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def makeConnected(self, n: int, connections: [[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        g = collections.defaultdict(set)
        for u, v in connections:
            g[u].add(v)
            g[v].add(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return 0
            
            visited.add(node)
            
            for adj in g[node]:
                dfs(adj)
            return 1

        return sum(dfs(i) for i in range(n)) - 1


    def get_cable_move(self, n: int, cables: [[int]]) -> int:
        if len(cables) < n - 1:
            return -1
        
        g = collections.defaultdict(set)
        for u, v in cables:
            g[u].add(v)
            g[v].add(u)

        visited = set()

        def dfs(node):
            q = [node]
            while q:
                node = q.pop()
                visited.add(node)
                
                for adj in g[node]:
                    if adj in visited:
                        continue
                    q += adj,
                
            return 1

        move = 0
        for node in range(n):
            if node not in visited:
                move += dfs(node)

        return move - 1


        #return sum(dfs(node) if node not in visited else 0 for node in range(n)) - 1


            
stime = time.time()
#print(1 == Solution().makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]]))

print(2 == Solution().makeConnected(6, [[0,1],[0,2],[0,3],[1,2], [2,3]]))
#print(2 == Solution().makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]))
#print(-1 == Solution().makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]))
#print(0 == Solution().makeConnected(n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]))
#print(4 == Solution().makeConnected(12, [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]))
print('elapse time: {} sec'.format(time.time() - stime))