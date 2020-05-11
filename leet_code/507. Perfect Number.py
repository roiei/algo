
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        inc = 0
        pdivisor = num
        divisor = (num + 1)//2
        if pdivisor == divisor:
            return False
        
        while divisor:
            if num%divisor == 0:
                inc += divisor
            
            pdivisor = divisor
            divisor = (divisor + 1)//2
            if pdivisor == divisor:
                break
        
        return inc == num
        

stime = time.time()
print(True == Solution().checkPerfectNumber(28))
print('elapse time: {} sec'.format(time.time() - stime))