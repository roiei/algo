import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a_win_cases = [
            {(0, 0), (1, 1), (2, 2)},
            {(0, 0), (0, 1), (0, 2)},
            {(0, 0), (1, 0), (2, 0)},
            {(2, 0), (2, 1), (2, 2)},
            {(0, 2), (1, 2), (2, 2)},
            {(0, 2), (1, 1), (2, 0)},
            {(0, 1), (1, 1), (2, 1)},
            {(1, 0), (1, 1), (1, 2)}
        ]
        
        b_win_cases = copy.deepcopy(a_win_cases)

        turn = True
        cnt = 0
        while moves:
            y, x = moves.pop(0)
            if turn:
                for case in a_win_cases:
                    case.discard((y, x))
                    if len(case) == 0:
                        return 'A'
            else:
                for case in b_win_cases:
                    case.discard((y, x))
                    if len(case) == 0:
                        return 'B'

            cnt += 1
            turn = not turn

        print(moves)
        print(a_win_cases)
        print(b_win_cases)

        if cnt < 9:
            return 'Pending'
    
        return 'Draw'


stime = time.time()
#print('B' == Solution().tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
#print("Draw" == Solution().tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
#print("Pending" == Solution().tictactoe([[0,0],[1,1]]))
print("A" == Solution().tictactoe([[1,2],[2,1],[1,0],[0,0],[0,1],[2,0],[1,1]]))
print('elapse time: {} sec'.format(time.time() - stime))