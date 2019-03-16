
# class Solution:
#     def reverse(x: 'int') -> 'int':

# sol = Solution()
# print(sol.reverse(x))


n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]


def traverse(graph, start):
    q = []
    q.append(start)
    visit[start] = True
    trace = []
    while q:
        cur = q.pop(0)
        visit[cur] = True
        trace.append(cur)
        print('visit = ', cur)
        for x in range(len(graph[cur])):
            if 1 == graph[cur][x]:
                if False == visit[x]:
                    q.append(x)
    return trace

def check_valid_trace(trace, n):
    valid = True
    for i in range(n):
        if 1 < trace.count(i):
            valid = False
    return valid

graph = [[0 for i in range(n)] for j in range(n)]
visit = [False for i in range(n)]

for edge in edges:
    graph[edge[0]][edge[1]] = 1
    graph[edge[1]][edge[0]] = 1

start = 0
trace = traverse(graph, start)
print(check_valid_trace(trace, n))

