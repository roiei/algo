import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    

    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        if not graph:
            return []
        n = len(graph)
        outdegree = [0]*n
        for i, adjs in enumerate(graph):
            outdegree[i] += len(adjs)
        leaves = [i for i, od in enumerate(outdegree) if od == 0]
        res = [*leaves]

        while leaves:
            nleaves = []
            for i in leaves:
                print('this = ', i)
                if True == self.is_cycle(i, graph, n):
                    continue
                for j in range(n):
                    
                    if j in nleaves:
                        continue
                    if i not in graph[j]:
                        continue
                    print('j = {}, adj = {}, deg = {}'.format(j, graph[j], outdegree[j]))
                    
                    outdegree[j] -= 1
                    if outdegree[j] == 0:
                        print('adding = ', j)
                        nleaves += j,
                        res += j,
            leaves = nleaves
        res.sort()
        return res

    def is_cycle(self, i, graph, n):
        q = [i]
        visit = [False]*n
        trace = []
        while q:
            cur = q.pop(0)
            if True == visit[cur]:
                continue
            visit[cur] = True
            trace += cur,
            for adj in graph[cur]:
                if adj in trace:
                    return True
                if visit[adj] == False:
                    q += adj,
        return False


    def isCyclic(self, g, vertex, path):
        path.add(vertex)
        for neighboor in g[vertex]:
            if neighboor in path:
                return True
            else:
                if neighboor in g and self.isCyclic(g, neighboor, path):
                    return True
        path.remove(vertex)
        return False

    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        if not graph:
            return []
        n = len(graph)
        res = []
        for i in range(n):
            if True != self.isCyclic(graph, i, set()):
                res += i,
        print(res)

        return res

    

    


    def dfs(self, i, graph, n):
        q = [i]
        visit = [False]*n
        trace = []
        cycle = False
        while q:
            cur = q.pop()
            if True == visit[cur]:
                continue
            visit[cur] = True
            trace += cur,
            for adj in graph[cur]:
                # print('cur = {}, adj = {}'.format(cur, adj))
                if adj in trace and visit[adj] == True:
                    if graph[adj]:
                        # print('cur = {}, adj = {}, trace = {}, visit[{}] = {}'.format(cur, adj, trace, adj, visit[adj]))
                        cycle = True
                if visit[adj] == False:
                    q += adj,
                # print('cur = {}, adj = {}, q = {}'.format(cur, adj, q))
        return trace, cycle

    def eventualSafeNodes(self, graph):
        n = len(graph)
        res = []
        for i, g in enumerate(graph):
            trace, cycle = self.dfs(i, graph, n)
            # print('trace of {}: {} -> {}'.format(i, trace, cycle))
            # print()
            if cycle == False:
                res += i,
        print(res)
        return res


    # void DFSUtil(boolean visited[], int i, Stack<Integer> st) {
    #     st.push(i);
    #     visited[i] = true;
    #     for (int k : adj[i]) {
    #         if (!visited[k])
    #             DFSUtil(visited, k, st);
    #         else if (st.contains(k))
    #             flag = 1;
    #     }
    #     if (flag != 1)
    #     st.pop();
    # }

    # void DFS() {
    #     Stack<Integer> st = new Stack<Integer>();
    #     boolean visited[] = new boolean[V];
    #     for (int i = 0; i < V; i++) {
    #         if (!visited[i])
    #             DFSUtil(visited, i, st);
    #     }
    # }

    def eventualSafeNodes(self, graph):
        n = len(graph)
        res = []
        visited = [False]*n
        stk = []
        for i, g in enumerate(graph):
            if True == visited[i]:
                continue

            def do_check(visited, i, stk):
                ret = False
                flag = 0
                stk += i,
                for adj in graph[i]:
                    if False == visited[adj]:
                        ret = do_check(visited, adj, stk)
                    elif adj in stk:
                        return True
                return ret


            if True == do_check(visited, i, stk):
                res += i,

            # print('trace of {}: {} -> {}'.format(i, trace, cycle))
            # print()
        print(res)


    def eventualSafeNodes(self, graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = collections.defaultdict(int)

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK
            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GRAY:
                    return False
                if not dfs(nei):
                    return False
            color[node] = BLACK
            return True

        res = []
        for i in [*range(len(graph))]:
            if True == dfs(i):
                res += i,
        return res

    def eventualSafeNodes(self, graph):
        # WHITE: not visit, GRAY: visiting, BLACK: visited(no cycle)
        WHITE, GRAY, BLACK = 0, 1, 2
        n = len(graph)
        state = [WHITE]*n
        
        def dfs(node):
            state[node] = GRAY
            
            for adj in graph[node]:
                if state[adj] == BLACK:
                    continue
                if state[adj] == GRAY:
                    return False
                res = dfs(adj)
                if False == res:
                    return False

            state[node] = BLACK
            return True
    
        res = []
        for node in range(n):
            ret = False
            if state[node] == WHITE:
                ret = dfs(node)
            elif state[node] == BLACK:
                ret = True
            
            if True == ret:
                res += node,
        return res


#  0     1       2             3       4         5         6     7     8  9
[[4,9],[3,5,7],[0,3,4,5,6,8],[7,8,9],[5,6,7,8],[6,7,8,9],[7,9],[8,9],[9],[]]



stime = time.time()
#print([0, 1, 2, 3] == Solution().eventualSafeNodes([[1, 2], [], [1, 3], [1]]))
print([] == Solution().eventualSafeNodes([[1, 2], [2], [3], [1]]))
#print([0,1,2,3,4] == Solution().eventualSafeNodes([[],[0,2,3,4],[3],[4],[]]))
#print([2,4,5,6] == Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
#print([0,1,2,3,4,5,6,7,8,9] == Solution().eventualSafeNodes([[4,9],[3,5,7],[0,3,4,5,6,8],[7,8,9],[5,6,7,8],[6,7,8,9],[7,9],[8,9],[9],[]]))
#print(Solution().eventualSafeNodes([[],[0,2,3,4],[3],[4],[]]))
#print(Solution().eventualSafeNodes([[0],[2,3,4],[3,4],[0,4],[]]))
#print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print('elapse time: {} sec'.format(time.time() - stime))

