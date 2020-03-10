import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def maximalSquare(self, matrix: 'List[List[str]]') -> int:
        if not matrix:
            return 0
        h = len(matrix)
        w = len(matrix[0])
        matrix = [[int(matrix[y][x]) for x in range(w)] for y in range(h)]
        for y in range(1, h):
            for x in range(1, w):
                if 0 == matrix[y][x]:
                    continue
                matrix[y][x] = min(matrix[y-1][x], 
                                   matrix[y][x-1], 
                                   matrix[y-1][x-1])+1
        return max([max(line) for line in matrix])**2



matrix = [["0","0","0","1"],
          ["1","1","0","1"],
          ["1","1","1","1"],
          ["0","1","1","1"],
          ["0","1","1","1"]]

stime = time.time()
print(Solution().maximalSquare(matrix))
print('elapse time: {} sec'.format(time.time() - stime))