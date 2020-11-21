
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache


"""
You are a hiker preparing for an upcoming hike. 
You are given heights, a 2D array of size rows x columns, 
where heights[row][col] represents the height of cell (row, col). 
You are situated in the top-left cell, (0, 0), 
and you hope to travel to the bottom-right cell,
(rows-1, columns-1) (i.e., 0-indexed). 

You can move up, down, left, or right, 
and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights 
between two consecutive cells of the route.

Return the minimum effort required to travel 
from the top-left cell to the bottom-right cell.

Explanation: The route of [1,3,5,3,5] has a maximum absolute difference 
of 2 in consecutive cells.

1,  3,  5,  3,  5
  2   2   2   2


This is better than the route of [1,2,2,2,5], 
where the maximum absolute difference is 3.

1,  2,  2,  2,  5
  1   0   0   3


1,  2,  2

3,  8,  2

5,  3,  5

"""


class Solution:

    def minimumEffortPath(self, heights: [[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        def dfs(y, x, visited, mx, pre_height):
            mx = max(mx, abs(pre_height - heights[y][x]))

            if y == rows - 1 and x == cols - 1:
                return mx

            res = float('inf')
            visited.add((y, x))

            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ny = y + dy
                nx = x + dx
                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue

                if (ny, nx) in visited:
                    continue
                
                res = min(res, dfs(ny, nx, visited, mx, heights[y][x]))
            
            visited.discard((y, x))
            return res

        return dfs(0, 0, set(), 0, heights[0][0])

    def minimumEffortPath(self, heights: [[int]]) -> int:
        """
        go to min diff but keep the max diff

        [1], 2, 2  -> (1)  [2]  2 -> (1) (2) [2] -> (1) (2) (2) -> (1) (2) (2)
         3,  8, 2      3    8   2     3   8   2      3   8  [2]    [3]  8  (2)
         5,  3, 5      5    3   5     5   3   5      5   3   5      5   3   5

         diff = 0      1              1              1              2

         (1) (2) (2) -> (1) (2) (2) -> (1) (2) (2)
         (3)  8  (2)    (3)  8  (2)    (3)  8  (2)
         [5]  3   5     (5) [3]  5     (5) (3) [5]

         2               2              2
        """
        rows = len(heights)
        cols = len(heights[0])

        q = [(0, 0, 0, heights[0][0])]
        visited = set()

        while q:
            while q:
                pre_mx, y, x, pre_height = heapq.heappop(q)
                if (y, x) not in visited:
                    break

            if y == rows - 1 and x == cols - 1:
                return pre_mx

            visited.add((y, x))

            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny = dy + y
                nx = dx + x
                if (ny, nx) in visited:
                    continue

                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue

                mx = max(pre_mx, abs(heights[ny][nx] - pre_height))
                heapq.heappush(q, (mx, ny, nx, heights[ny][nx]))


stime = time.time()
print(2 == Solution().minimumEffortPath(heights = 
    [[1,2,2],
     [3,8,2],
     [5,3,5]]))
# print(1 == Solution().minimumEffortPath(heights = 
#     [[1,2,3],[3,8,4],[5,3,5]]))
# print(0 == Solution().minimumEffortPath(heights = \
#     [[1,2,1,1,1],
#      [1,2,1,2,1],
#      [1,2,1,2,1],
#      [1,2,1,2,1],
#      [1,1,1,2,1]]))
print('elapse time: {} sec'.format(time.time() - stime))
