
class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        graph = [[0 for i in range(numCourses)] for i in range(numCourses)]
        visit = [False for i in range(numCourses)]
        trace = []

        if not prerequisites:
            return True

        for row in prerequisites:
            for i in range(len(row)):
                if i+1 >= len(row):
                    continue
                graph[row[i]][row[i+1]] = 1

        for start in range(numCourses):
            visit = [False for i in range(numCourses)]
            stk = []
            stk.append(start)
            ret = True
            while stk:
                cur = stk.pop()
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

    def findOrder(self, n: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        graph = [[0 for i in range(n)] for j in range(n)]
        visit = [False for i in range(n)]
        indegree = [0 for i in range(n)]
        outdegree = [0 for i in range(n)]

        if not prerequisites:
            return [i for i in range(n)][::-1]
        # if False == self.canFinish(n, prerequisites):
        #     return []

        # link
        for item in prerequisites:
            graph[item[0]][item[1]] = 1
        for s in range(len(graph)):
            for t in range(len(graph[0])):
                if 1 == graph[s][t]:
                    indegree[t] += 1
        for s in range(len(graph)):
            outdegree[s] = graph[s].count(1)

        start = -1
        for i in range(len(graph)):
            if 0 == indegree[i] and outdegree[i] > 0:
                start = i
                break
        if -1 == start:
            return []

        q = []
        q.append(start)
        trace = []

        while q:
            cur = q.pop(0)
            trace.append(cur)
            visit[cur] = True
            # print('visit: {} -> '.format(cur))
            for adj in range(len(graph[cur])):
                if 0 == graph[cur][adj]:
                    continue
                if 0 < indegree[adj]:
                    indegree[adj] -= 1
                #if 0 == indegree[adj]:
                #    q.append(adj)
            for i in range(len(graph)):
                if False == visit[i] and 0 == indegree[i]:
                    q.append(i)
                    break

        print('visit = ', trace[::-1])
        return trace[::-1]


numCourses = 2
prerequisites = [[1, 0]]
#prerequisites = [[1,0],[0,1]]
#prerequisites = [[0,1],[1,0]]
# numCourses = 1
# prerequisites = []
#numCourses = 3
#prerequisites = [[1,0],[2,0],[0,2]]

numCourses = 3
prerequisites = [[0,1],[0,2],[1,2]]
# prerequisites = [[1,0],[0,2],[2,1]]
# prerequisites = [[1,2],[1,0],[0,2]]
# numCourses = 4
# prerequisites = [[0,1],[3,1],[1,3],[3,2]]
# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]

# numCourses = 2
# #prerequisites = []
# prerequisites = [[0,1],[1,0]]

numCourses = 3
prerequisites = [[1,0]]
prerequisites = [[0,2],[1,2],[2,0]]

# numCourses = 4
# prerequisites = [[3,0],[0,1]]

# numCourses = 10
# prerequisites = [[5,8],[3,5],[1,9],[4,5],[0,2],[7,8],[4,9]]

s = Solution()
print(s.findOrder(numCourses, prerequisites))

