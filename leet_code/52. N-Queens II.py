import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [-1]*n
        num = 0

        def check(board, n, dep):
            nonlocal num
            for pdep in range(dep):
                if (board[pdep] == board[dep] or 
                    dep-pdep == abs(board[dep]-board[pdep])):
                    return True
            if dep == n-1:
                num += 1
                return

            for i in range(n):
                board[dep+1] = i
                check(board, n, dep+1)

        res = []
        for i in range(n):
            board[0] = i
            check(board, n, 0)
        return num


stime = time.time()
print(Solution().solveNQueens(4))
print('elapse time: {} sec'.format(time.time() - stime))