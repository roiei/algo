import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        n = len(distance)
        clkwise_g = collections.defaultdict(dict)
        cclkwise_g = collections.defaultdict(dict)

        for i in range(n - 1):
            clkwise_g[i][i + 1] = distance[i]           
        clkwise_g[n - 1][0] = distance[-1]

        for i in range(n - 1, 0, -1):
            cclkwise_g[i][i - 1] = distance[i - 1]
        cclkwise_g[0][n - 1] = distance[-1]


        def traverse(start, end, g):
            q = [(start, 0)]
            visited = set()
            visited.add(start)
            tot_cost = 0

            while q:
                node, tot_cost = q.pop(0)
                if node == end:
                    break
                for adj, dist in g[node].items():
                    if adj in visited:
                        continue
                    visited.add(adj)
                    q += (adj, tot_cost + dist),

            return tot_cost

        return min(traverse(start, destination, clkwise_g), \
                   traverse(start, destination, cclkwise_g))


stime = time.time()
print(1 == Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1))
print(3 == Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2))
print('elapse time: {} sec'.format(time.time() - stime))


