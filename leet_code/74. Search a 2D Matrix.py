import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix:
            return False
        cols = len(matrix[0])
        rows = len(matrix)
        
        for line in matrix:
            l = 0
            r = cols-1
            while l <= r:
                m = (l + r)//2
                if line[m] == target:
                    return True
                if line[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3


matrix = [
    [1, 3, 5, 7],
    [10,11,16,20],
    [23,30,34,50]]
target = 5

stime = time.time()
print(Solution().searchMatrix([
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]], 
5))
print('elapse time: {} sec'.format(time.time() - stime))