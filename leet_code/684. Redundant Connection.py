import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq



class Solution(object):
    def findRedundantConnection(self, edges):
        graph = {}
        
        def is_way_exist(s, d):
            visit = set()            
            q = [s]
            while q:
                cur = q.pop()
                if cur in visit:
                    continue
                if cur == d:
                    return True
                visit.add(cur)
                for adj in graph[cur]:
                    if adj in visit:
                        continue
                    q += adj,
            return False
        
        for u, v in edges:
            if u in graph and v in graph:
                if True == is_way_exist(u, v):
                    return u, v
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u] += v,
            graph[v] += u,
            
        return []

    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(list)
        
        def is_way_exist(s, d):
            visit = set()            
            q = [s]
            while q:
                cur = q.pop()
                if cur in visit:
                    continue
                if cur == d:
                    return True
                visit.add(cur)
                for adj in graph[cur]:
                    if adj in visit:
                        continue
                    q += adj,
            return False
        
        for u, v in edges:
            if u in graph and v in graph:
                if True == is_way_exist(u, v):
                    return u, v
            graph[u] += v,
            graph[v] += u,
            
        return []


    def findRedundantConnection(self, edges):
        g = collections.defaultdict(list)

        def is_connected(src, dst):
            q = [src]
            visit = set()

            while q:
                cur = q.pop()
                if cur == dst:
                    return True
                visit.add(cur)

                for adj in g[cur]:
                    if adj not in visit:
                        q += adj,
            return False

        for src, sink in edges:
            if src in g and sink in g:
                if True == is_connected(src, sink):
                    return [src, sink]
            g[src] += sink,
            g[sink] += src,

        return []

            

stime = time.time()
print([1,3] == Solution().findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]))
#print(-5 == Solution().findRedundantConnection([[-5]], 1))
#print(2 == Solution().findRedundantConnection([[1,2],[1,3]], 3))
print('elapse time: {} sec'.format(time.time() - stime))


