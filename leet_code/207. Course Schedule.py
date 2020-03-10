import collections


class Solution(object):
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        if not prerequisites:
            return True

        graph = [[0 for i in range(numCourses)] for i in range(numCourses)]
        visit = [False for i in range(numCourses)]
        trace = []

        for row in prerequisites:
            for i in range(len(row)):
                if i+1 >= len(row):
                    continue
                graph[row[i]][row[i+1]] = 1  # directed

        for start in range(numCourses):
            visit = [False for i in range(numCourses)]
            stk = []
            stk.append(start)
            ret = True

            while stk:
                cur = stk.pop()          # DFS
                visit[cur] = True
                for x in range(len(graph[cur])):
                    if 1 == graph[cur][x]:
                        if False == visit[x]:
                            stk.append(x)
                        elif x == start:
                            ret = False
            if False == ret:
                break
        return ret


    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        
        g = collections.defaultdict(list)
        
        for src, dst in prerequisites:
            g[src] += dst,
        
        for i in range(numCourses):
            visit = []
            q = [i]
            while q:
                cur = q.pop()
                visit += cur,
                for adj in g[cur]:
                    if adj not in visit:
                        q += adj,
                    elif adj == i:
                        return False
        
        return True


    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        
        g = collections.defaultdict(list)
        
        for src, dst in prerequisites:
            if dst in g:
                stk = []
                stk += g[dst]
                
                while stk:
                    cur = stk.pop()
                    if cur == src:
                        return False
                    
                    for adj in g[cur]:
                        stk += adj,

            g[src] += dst,

        return True


    def canFinish(self, numCourses, prerequisites):
        g = collections.defaultdict(list)

        for src, sink in prerequisites:
            g[src] += sink,
        
        indegree = [0]*numCourses
        for i in range(numCourses):
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
                    visit += cur,

        return len(visit) == numCourses


#print(True == Solution().canFinish(2, [[1,0]]))
# print(False == Solution().canFinish(4, [[0,1],[3,1],[1,3],[3,2]]))
# print(False == Solution().canFinish(4, [[0,1],[2,3],[1,2],[3,0]]))
print(False == Solution().canFinish(2, [[0,1],[1,0]]))