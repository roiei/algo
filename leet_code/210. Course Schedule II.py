import time
import collections


class Solution:
    def findOrder(self, n: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        g = collections.defaultdict(list)

        for src, sink in prerequisites:
            g[src] += sink,
        
        indegree = [0]*n
        for i in range(n):
            for adj in g[i]:
                indegree[adj] += 1
        
        q = [i for i in range(len(indegree)) if indegree[i] == 0]
        visit = q[:]

        while q:
            cur = q.pop(0)
            for adj in g[cur]:
                indegree[adj] -= 1
                
                if adj in visit:
                    continue
                
                if indegree[adj] == 0:
                    q += adj,
                    visit += adj,

        if len(visit) == n:
            return visit[::-1]
        return []

    def findOrder(self, n: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        g = collections.defaultdict(list)
        inbound = collections.defaultdict(int)
        
        for u, v in prerequisites:
            g[u] += v,
            inbound[u] = inbound[u]
            inbound[v] += 1
        
        q = [i for i in range(n) if inbound[i] == 0]
        visited = set(node for node in q)
        seq = []
        
        while q:
            u = q.pop(0)
            seq += u,
            
            for v in g[u]:
                if v in visited:
                    continue
                
                inbound[v] -= 1
                
                if inbound[v] == 0:
                    visited.add(v)
                    q += v,
        
        return seq[::-1] if len(seq) == n else []


stime = time.time()
#print([1, 3, 2, 4] == Solution().findOrder([1, 2, 4, 3]))
#print([0] == Solution().findOrder(1, []))
print([] == Solution().findOrder(3, [[0,2],[1,2],[2,0]]))
print('elapse time: {} sec'.format(time.time() - stime))