
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def matrixBlockSum(self, mat: [[int]], K: int) -> [[int]]:
        rows, cols = len(mat), len(mat[0])
        acc = [[0]*cols for _ in range(rows)]

        for y in range(rows):
            for x in range(cols):
                acc[y][x] = mat[y][x]
                if x > 0:
                    acc[y][x] += acc[y][x - 1]

        for y in range(rows):
            for x in range(cols):
                if y > 0:
                    acc[y][x] += acc[y - 1][x]


        res = [[0]*cols for _ in range(rows)]
        
        for y in range(rows):
            for x in range(cols):
                miny, maxy = max(0, y - K), min(rows - 1, y + K)
                minx, maxx = max(0, x - K), min(cols - 1, x + K)

                res[y][x] = acc[maxy][maxx]

                if miny > 0:
                    res[y][x] -= acc[miny - 1][maxx]

                if minx > 0:
                    res[y][x] -= acc[maxy][minx - 1]

                if miny > 0 and minx > 0:
                    res[y][x] += acc[miny - 1][minx - 1]

        return res

            
stime = time.time()
print([[12,21,16],[27,45,33],[24,39,28]] == Solution().matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))
print('elapse time: {} sec'.format(time.time() - stime))