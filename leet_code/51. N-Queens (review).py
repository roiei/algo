import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> 'List[List[str]]':
        board = [['.']*n for _ in range(n)]
        positions = [-1]*n

        def dfs(positions, depth):
            nonlocal res
            for i in range(depth):
                if (positions[i] == positions[depth] or   # x-axis
                    depth - i == abs(positions[depth] - positions[i])):  # y
                    return

            if depth == n - 1:
                res += [''.join(line) for line in board],
                return

            for i in range(n):
                positions[depth + 1] = i
                board[depth + 1][i] = 'Q'
                dfs(positions, depth + 1)
                board[depth + 1][i] = '.'

        res = []
        for i in range(n):
            positions[0] = i
            board[0][i] = 'Q'
            dfs(positions, 0)
            board[0][i] = '.'

        return res

    def solveNQueens(self, n: int) -> 'List[List[str]]':
        xpos = [-1]*n
        board = [['.']*n for _ in range(n)]
        res = []
        
        def dfs(board, xpos, y, n):
            nonlocal res
            
            if y == n:
                res += [''.join(line) for line in board],
                return
          
            for x in range(n):
                for pre_y in range(y):
                    if (x == xpos[pre_y] or
                        y - pre_y == abs(x - xpos[pre_y])):
                        break
                else:
                    board[y][x] = 'Q'
                    xpos[y] = x
                    dfs(board, xpos, y + 1, n)
                    board[y][x] = '.'
        
        dfs(board, xpos, 0, n)
        return res

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        pos = [-1]*n
        res = []

        def dfs(y, res):
            if y == n:
                res += [''.join(line) for line in board],
                return

            for x in range(n):
                for py in range(y):
                    if pos[py] == x or \
                       y - py == abs(x - pos[py]):
                       break
                else:
                    pos[y] = x
                    board[y][x] = 'Q'
                    dfs(y + 1, res)
                    board[y][x] = '.'

        dfs(0, res)
        return res


stime = time.time()
print(Solution().solveNQueens(4))
print('elapse time: {} sec'.format(time.time() - stime))