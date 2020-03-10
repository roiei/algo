import time
from util_list import *
from util_tree import *
import copy
import collections



class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        for r in range(rows):
            f = {}
            for c in range(cols):
                if '.' == board[r][c]:
                    continue
                if board[r][c] not in f:
                    f[board[r][c]] = True
                else:
                    print(f'1. (r,c) = ({r}, {c}), {board[r][c]}')
                    return False
        for c in range(cols):
            f = {}
            for r in range(rows):
                if '.' == board[r][c]:
                    continue
                if board[r][c] not in f:
                    f[board[r][c]] = True
                else:
                    print(f'2. (r,c) = ({r}, {c}), {board[r][c]}')
                    return False

        offsets = [(0, 0), (0, 3), (0, 6),
                   (3, 0), (3, 3), (3, 6),
                   (6, 0), (6, 3), (6, 6)]
        for offset in offsets:
            f = {}
            for r in range(offset[0], offset[0]+3):
                for c in range(offset[1], offset[1]+3):
                    if '.' == board[r][c]:
                        continue
                    if board[r][c] not in f:
                        f[board[r][c]] = True
                    else:
                        print(f'3. (r,c) = ({r}, {c}), {board[r][c]}')
                        return False
        return True

            

board = [
["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]
expected = True

board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]
expected = True

stime = time.time()
print(expected == Solution().isValidSudoku(board))
print('elapse time: {} sec'.format(time.time() - stime))