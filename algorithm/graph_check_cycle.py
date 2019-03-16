


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
                print('{} -> '.format(cur))
                visit[cur] = True
                for x in range(len(graph[cur])):
                    if 1 == graph[cur][x]:
                        if False == visit[x]:
                            stk.append(x)
                        elif x == start:
                            ret = False
            if False == ret:
                break
            print()
        return ret


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


s = Solution()
print(s.canFinish(numCourses, prerequisites))

