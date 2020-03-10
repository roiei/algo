import time


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


stime = time.time()
print([1, 3, 2, 4] == Solution().findOrder([1, 2, 4, 3]))
print('elapse time: {} sec'.format(time.time() - stime))