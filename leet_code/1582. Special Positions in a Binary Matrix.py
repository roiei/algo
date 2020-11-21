import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def numSpecial(self, mat: [[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        
        rlines = []
        
        for x in range(cols):
            rline = []
            for y in range(rows):
                rline += mat[y][x],
            
            rlines += rline.count(1),
        
        clines = []
        for line in mat:
            clines += line.count(1),
        
        cnt = 0

        for y in range(rows):
            for x in range(cols):
                if mat[y][x] == 1:
                    if 1 == rlines[x] and 1 == clines[y]:
                        cnt += 1
        
        return cnt


stime = time.time()
print(2 == Solution().numSpecial(
    [[0,0,1,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,1,0,0]])
)
print('elapse time: {} sec'.format(time.time() - stime))

