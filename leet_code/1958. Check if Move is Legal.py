import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List
import math
import functools
import heapq


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            y = rMove
            x = cMove
            line = []

            while 0 <= y + oy < rows and 0 <= x + ox < cols:
                y += oy
                x += ox
                line += board[y][x],

            if len(line) >= 3:
                line[0] == line[-1]
                for i in range(1, len(line) - 1):
                    if line[i] == line[0]:
                        break




stime = time.time()
print(True == Solution().checkMove(
    board = 
    [[".",".",".","B",".",".",".","."]
    ,[".",".",".","W",".",".",".","."]
    ,[".",".",".","W",".",".",".","."]
    ,[".",".",".","W",".",".",".","."]
    ,["W","B","B",".","W","W","W","B"]
    ,[".",".",".","B",".",".",".","."]
    ,[".",".",".","B",".",".",".","."]
    ,[".",".",".","W",".",".",".","."]], 
    rMove = 4, cMove = 3, color = "B"))
print('elapse time: {} sec'.format(time.time() - stime))