
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: [[int]], blue_edges: [[int]]) -> [int]:
        
        g = collections.defaultdict(list)
        visited = set()
        q = [(0, 'RED', 0)]    # node, color, depth
        q += (0, 'BLUE', 0),

        for u, v in red_edges:
            g[u] += (v, 'RED'),
        for u, v in blue_edges:
            g[u] += (v, 'BLUE'),

        res = [-1]*(n)

        while q:
            node, clr, depth = q.pop(0)
            if node not in visited:
                visited.add((node, clr))
                if res[node] == -1:
                    res[node] = depth

            for adj, adj_clr in g[node]:
                if (adj, adj_clr) in visited:
                    continue
                if adj_clr == clr:
                    continue

                q += (adj, adj_clr, depth + 1),

        return res


    # not working: only differnce is dict and list
    # it means that two link can exist on the same nodes
    # so, it is not possible to use the dict for the graph in this case.
    #
    def shortestAlternatingPaths(self, n: int, red_edges: [[int]], blue_edges: [[int]]) -> [int]:

        g = collections.defaultdict(list)
        visited = set()
        q = [(0, 'RED', 0)]    # node, color, depth
        q += (0, 'BLUE', 0),

        for u, v in red_edges:
            g[u][v] = 'RED',
        for u, v in blue_edges:
            g[u][v] = 'BLUE',

        res = [-1]*(n)

        while q:
            node, clr, depth = q.pop(0)
            if node not in visited:
                visited.add((node, clr))
                if res[node] == -1:
                    res[node] = depth

            for adj, adj_clr in g[node].items():
                if (adj, adj_clr) in visited:
                    continue
                if adj_clr == clr:
                    continue

                q += (adj, adj_clr, depth + 1),

        return res



stime = time.time()
print([0,1,1] == Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]))
print('elapse time: {} sec'.format(time.time() - stime))