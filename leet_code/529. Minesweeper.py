import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections



class Solution:
    def updateBoard(self, board: [[str]], click: [int]) -> [[str]]:
        rows = len(board)
        cols = len(board[0])

        def dfs(board, y, x):
            if board[y][x] == 'M':
                board[y][x] = 'X'
                return
            if board[y][x] == 'B' or ('1' <= board[y][x] <= '8'):
                return
            cnt = 0
            adjs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for oy, ox in adjs:
                ny, nx = y+oy, x+ox
                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue
                if 'M' == board[ny][nx]:
                    cnt += 1
            if cnt == 0:
                board[y][x] = 'B'
                for oy, ox in adjs:
                    ny, nx = y+oy, x+ox
                    if not (0 <= ny < rows and 0 <= nx < cols):
                        continue
                    dfs(board, ny, nx)
            else:
                board[y][x] = str(cnt)

        dfs(board, click[0], click[1])
        return board


board = [
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
click = [3, 0]

stime = time.time()
print(Solution().updateBoard(board, click))
print('elapse time: {} sec'.format(time.time() - stime))

