import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for y in range(n):
            cnts = [0]*n

            for x in range(n):
                cnts[matrix[y][x] - 1] += 1

            if cnts != [1]*n:
                return False

        for x in range(n):
            cnts = [0]*n

            for y in range(n):
                cnts[matrix[y][x] - 1] += 1

            if cnts != [1]*n:
                return False

        return True


stime = time.time()
print(True == Solution().checkValid(matrix = [[1,2,3],[3,1,2],[2,3,1]]))
print(False == Solution().checkValid(matrix = [[1,1,1],[1,2,3],[1,2,3]]))
print('elapse time: {} sec'.format(time.time() - stime))