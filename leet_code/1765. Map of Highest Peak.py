import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        
        output = [[float('inf')]*cols for _ in range(rows)]
        
        inits = []
        for y in range(rows):
            for x in range(cols):
                if isWater[y][x] == 1:  # 1 = water
                    inits += (y, x),
                    output[y][x] = 0

        for iy, ix in inits:
            q = [(iy, ix, 0)]
            visited = set((iy, ix))
            
            while q:
                y, x, height = q.pop(0)
                output[y][x] = min(output[y][x], height)

                for oy, ox in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    ny = y + oy
                    nx = x + ox

                    if not (0 <= ny < rows and 0 <= nx < cols):
                        continue

                    if isWater[ny][nx] == 1:
                        continue
                    
                    if (ny, nx) in visited:
                        continue

                    if output[ny][nx] < height + 1:
                        continue

                    visited.add((ny, nx))
                    q += (ny, nx, height + 1),
        
        return output

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        
        output = [[float('inf')]*cols for _ in range(rows)]
        
        q = []
        for y in range(rows):
            for x in range(cols):
                if isWater[y][x] == 1:  # 1 = water
                    q += (y, x),
                    output[y][x] = 0

        visited = set(q)
        height = 0

        while q:
            nq = []
            for y, x in q:
                output[y][x] = height

                for oy, ox in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    ny = y + oy
                    nx = x + ox

                    if not (0 <= ny < rows and 0 <= nx < cols):
                        continue

                    if (ny, nx) in visited:
                        continue

                    nq += (ny, nx),
                    visited.add((ny, nx))

            q = nq
            height += 1
    
        return output

                
stime = time.time()
print([[1,1,0],
       [0,1,1],
       [1,2,2]] == Solution().highestPeak(
    isWater = [[0,0,1],
               [1,0,0],
               [0,0,0]]))
print('elapse time: {} sec'.format(time.time() - stime))
