
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def maxStudents(self, seats: [[str]]) -> int:
        rows = len(seats)
        cols = len(seats[0])
        starts = []

        for y in range(rows):
            for x in range(cols):
                if seats[y][x] == '.':
                    starts += (y, x),

        #g = collections.defaultdict(list)


        cnt = 0
        visited = set()

        for sy, sx in starts:
            if (sy, sx) in visited:
                continue
            
            visited.add((sy, sx))
            q = [(sy, sx)]

            while q:
                y, x = q.pop(0)

                for ny, nx in [(y - 1, x - 1), (y - 1, x + 1), (y, x - 1), (x, x + 1), \
                    (y + 1, x + 1), (y + 1, x - 1)]:
                    if not (0 <= ny < rows and 0 <= nx < cols):
                        continue

                    if (ny, nx) in visited:
                        continue

                    q += (ny, nx),
                    visited.add((ny, nx))

            cnt += 1

        print(cnt)
        return cnt


    def maxStudents(self, seats: [[str]]) -> int:
        rows = len(seats)
        cols = len(seats[0])

        mx = 2**rows
        dp = [0]*mx
        
        for x in range(cols):
            n_dp = [0]*mx

            for i in range(mx):
                cnt = 0

                for y in range(rows):
                    t = (1<<y)&i
                    if t:
                        cnt += 1
                    if t and seats[y][x] == '#':
                        break
                else:
                    for j in range(mx):
                        if ((i | (i >> 1)) & j) == 0 and ((j | j >> 1) & i == 0):
                            n_dp[i] = max(n_dp[i], dp[j] + cnt)

                
            dp = n_dp

        return max(dp)

            



            
stime = time.time()
print(4 == Solution().maxStudents(seats = 
               [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]))
print(3 == Solution().maxStudents(seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]))
print(10 == Solution().maxStudents(seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]))
print('elapse time: {} sec'.format(time.time() - stime))