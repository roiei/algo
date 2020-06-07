
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def countBattleships(self, board: [[str]]) -> int:
        def dfs(y, x, trace, visited):
            if board[y][x] == '.':
                return
            if (y, x) in visited:
                return

            visited.add((y, x))
            trace.add((y, x))

            for oy, ox in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                oy += y
                ox += x
                if not (0 <= oy < rows and 0 <= ox < cols):
                    continue
                dfs(oy, ox, trace, visited)

        def is_valid(trace):
            trace = list(trace)
            fy, fx = trace.pop(0)

            for y, x in trace:
                if y != fy:
                    break
            else:
                return True

            for y, x in trace:
                if x != fx:
                    return False

            return True


        rows = len(board)
        cols = len(board[0])
        visited = set()
        cnt = 0

        for y in range(rows):
            for x in range(cols):
                if board[y][x] == '.':
                    continue
                if (y, x) in visited:
                    continue
                trace = set()
                dfs(y, x, trace, visited)
                if is_valid(trace):
                    cnt += 1
                visited |= trace

        return cnt


stime = time.time()
print(2 == Solution().countBattleships(['X..X',
'...X',
'...X']))

print(40 == Solution().countBattleships([["X","X","X",".","X",".","X",".","X","X","X","X","X","X","X"],[".",".",".","X",".","X",".","X",".",".",".",".",".",".","."],[".","X","X",".",".","X",".",".","X","X","X","X",".","X","."],["X",".",".",".",".",".",".",".",".",".",".",".","X",".","X"],[".","X","X","X","X","X","X","X",".","X","X",".","X",".","X"],["X",".",".",".",".",".",".",".","X",".",".",".","X",".","X"],["X",".",".","X",".","X",".","X",".","X","X",".","X",".","X"],[".","X","X",".",".",".",".",".",".",".",".",".",".",".","."],["X",".",".","X","X","X","X","X","X","X","X","X","X","X","X"],[".","X",".",".",".",".",".",".",".",".",".",".",".",".","."],[".","X",".","X","X",".","X",".","X",".","X",".","X",".","."],["X",".",".",".",".",".",".",".",".","X",".",".","X",".","X"],[".","X","X","X",".","X","X","X",".",".","X",".","X",".","X"],["X",".",".",".",".",".",".",".",".",".",".","X",".",".","."],[".","X","X","X","X","X","X","X","X","X",".",".",".","X","X"]]))

print('elapse time: {} sec'.format(time.time() - stime))