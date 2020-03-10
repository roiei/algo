
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def diagonalSort(self, mat: [[int]]) -> [[int]]:

        def fill_diag(sy, sx):
            y = sy
            x = sx
            diag = []

            while y < m and x < n:
                diag += mat[y][x],
                y += 1
                x += 1
            
            diag.sort()

            i = 0
            y = sy
            x = sx

            while y < m and x < n:
                res[y][x] = diag[i]
                i += 1
                y += 1
                x += 1


        m = len(mat)
        n = len(mat[0])
        
        res = [[0]*n for _ in range(m)]
        
        for sy in range(m - 1, -1, -1):
            fill_diag(sy, 0)

        for sx in range(1, n, 1):
            fill_diag(0, sx)
        
        return res

            
stime = time.time()
print([[1,1,1,1],[1,2,2,2],[1,2,3,3]] == Solution().diagonalSort(mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
print('elapse time: {} sec'.format(time.time() - stime))