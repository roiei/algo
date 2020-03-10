
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        lines = [[] for _ in range(numRows)]
        forward = False
        y = 0
        
        for ch in s:
            lines[y] += ch,
            
            if y == numRows - 1 or y == 0:
                forward = not forward
                
            if forward:
                y += 1
            else:
                y -= 1
        
        return ''.join([''.join(line) for line in lines])
    


stime = time.time()
print("PINALSIGYAHRPI" == Solution().convert("PAYPALISHIRING", 4))
print('elapse time: {} sec'.format(time.time() - stime))