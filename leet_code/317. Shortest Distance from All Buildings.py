import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
from typing import List


class Solution:
    def shortestDistance(self, grid):
        def bfs(grid, all_dists, reachable_num, y, x):
            q = [(y, x, 1)]
            visited = set((y, x))

            while q:
                y, x, dist = q.pop(0)
                for oy, ox in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = oy + y, ox + x
                    if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] == 0 \
                        and (ny, nx) not in visited:
                            
                        reachable_num[ny][nx] += 1
                        all_dists[ny][nx] += dist
                        q += (ny, nx, dist + 1),
                        visited.add((ny, nx))
 
 
        m, n = len(grid),  len(grid[0])
        all_dists = [[0 for _ in range(n)] for _ in range(m)]
        reachable_num = [[0 for _ in range(n)] for _ in range(m)]
        num_buildings = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_buildings += 1
                    bfs(grid, all_dists, reachable_num, i, j)
 
        shortest = float("inf")
        for y in range(m):
            for x in range(n):
                if all_dists[y][x] < shortest and reachable_num[y][x] == num_buildings:
                    shortest = all_dists[y][x]
 
        return shortest if shortest != float("inf") else -1

    def shortestDistance(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def dfs(y, x):
            q = [(y, x, 0)]
            visited = set((y, x))

            while q:
                y, x, dist = q.pop(0)

                for oy, ox in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = oy + y, ox + x

                    if not (0 <= ny < rows and 0 <= nx < cols):
                        continue
                    if grid[ny][nx] != 0:
                        continue
                    if (ny, nx) in visited:
                        continue
                    
                    q += (ny, nx, dist + 1),
                    dists[ny][nx] += dist + 1
                    building_nums[ny][nx] += 1
                    visited.add((ny, nx))

        dists = [[0]*cols for _ in range(rows)]
        building_nums = [[0]*cols for _ in range(rows)]
        tot_buildings = 0

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 1:
                    dfs(y, x)
                    tot_buildings += 1
        
        mn = float('inf')
        for y in range(rows):
            for x in range(cols):
                if building_nums[y][x] != tot_buildings:
                    continue
                
                mn = min(mn, dists[y][x])
        
        return mn if mn != float('inf') else -1


stime = time.time()
print(7 == Solution().shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
print('elapse time: {} sec'.format(time.time() - stime))