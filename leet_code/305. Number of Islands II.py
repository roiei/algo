
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        res = []
        g = collections.defaultdict(list)

        for y, x in operators:
            print(y, x)
            g[(y, x)] = list()

            for oy, ox in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not (0 <= y + oy < n and 0 <= x + ox < m):
                    continue

                if (y + oy, x + ox) in g.keys():
                    if (y + oy, x + ox) not in g[(y, x)]:
                        g[(y, x)] += (y + oy, x + ox),

                    if (y, x) not in g[(y + oy, x + ox)]:
                        g[(y + oy, x + ox)] += (y, x),

            visited = set()
            cnt = 0

            for y, x in operators:
                if (y, x) in visited:
                    continue

                if (y, x) not in g:
                    continue

                q = [(y, x)]
                visited.add((y, x))

                while q:
                    y, x in q.pop(0)

                    for ay, ax in g[(y, x)]:
                        if (ay, ax) in visited:
                            continue

                        visited.add((ay, ax))
                        q += (ay, ax),

                cnt += 1

            res += cnt,

        print(res)
        return res






stime = time.time()
print([1,1,2,2] == Solution().numIslands2(n = 4, m = 5, operators = [[1,1],[0,1],[3,3],[3,4]]))

# [1,2,1,1]
# 2
# 2
# [[0,0],[1,1],[1,0],[0,1]]
print('elapse time: {} sec'.format(time.time() - stime))