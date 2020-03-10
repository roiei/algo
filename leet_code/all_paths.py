
class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        trace = {}
        for i in range(n-2, -1, -1):
            trace[i] = []
            for j in range(len(graph[i])):
                if graph[i][j] == n-1:
                    trace[i].append([i, n-1])
                    continue
                if graph[i][j] in trace:
                    for k in trace[graph[i][j]]:
                        trace[i].append([i] + k)
        return trace[0]


graph = [[1,2], [3], [3], []]  # [[0,1,3],[0,2,3]] 

stime = time.time()
sol = Solution()
ret = sol.allPathsSourceTarget(graph)
print('elapse time: {} sec'.format(time.time() - stime))
print(ret)