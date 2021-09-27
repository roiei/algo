import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        cols = len(points[0])
        weights = [[0]*cols for _ in range(cols)]

        for x in range(cols):
            for i in range(cols):
                weights[x][i] = abs(x - i)

        for y in range(rows - 1):
            for x in range(cols):
                mx = 0
                for i in range(cols):
                    mx = max(mx, points[y][i] - weights[x][i])

                points[y + 1][x] += mx

        return max(points[-1])

    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        cols = len(points[0])

        for y in range(rows - 1):
            for x in range(cols - 2, -1, -1):
                points[y][x] = max(points[y][x], points[y][x + 1] - 1)

            for x in range(cols):
                points[y][x] = max(points[y][x], points[y][x - 1] - 1 if x > 0 else 0)
                points[y + 1][x] += points[y][x]

        return max(points[-1])



stime = time.time()
print(9 == Solution().maxPoints([[1,2,3],[1,5,1],[3,1,1]]))
print('elapse time: {} sec'.format(time.time() - stime))