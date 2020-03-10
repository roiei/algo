import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        for sroot in range(int(c**0.5)+1):
            squares.add(sroot**2)
            search = c - sroot*sroot
            if search in squares:
                return True
        return False


stime = time.time()
#print(Solution().judgeSquareSum(5))
print(Solution().judgeSquareSum(1000))
print('elapse time: {} sec'.format(time.time() - stime))
