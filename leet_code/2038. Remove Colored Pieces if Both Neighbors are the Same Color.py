import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math



class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        acnt = 0
        bcnt = 0
        
        for i in range(1, len(colors) - 1):
            if colors[i] == 'A':
                if colors[i - 1] == colors[i] == colors[i + 1]:
                    acnt += 1

            if colors[i] == 'B':
                if colors[i - 1] == colors[i] == colors[i + 1]:
                    bcnt += 1
        
        return acnt > bcnt


stime = time.time()
print(True == Solution().winnerOfGame(colors = "AAABABB"))
print('elapse time: {} sec'.format(time.time() - stime))