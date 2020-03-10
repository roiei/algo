import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findNthDigit(self, n: int) -> int:
        cnt = 1
        step = 9
        while n > step:
            cnt += 1
            n -= step
            step = 9*cnt*10**(cnt - 1)

        idx = (n-1)//cnt
        base = int('1' + '0'*(cnt-1))
        base = str(base + idx)
        i = (n-1)%cnt
        return int(base[i])


stime = time.time()
#print(3 == Solution().findNthDigit(3))
#print(1 == Solution().findNthDigit(10))
print(0 == Solution().findNthDigit(11))
#print(2 == Solution().findNthDigit(15))
#print(3 == Solution().findNthDigit(1000))
#print(7 == Solution().findNthDigit(10000))
#print(1 == Solution().findNthDigit(190))
print('elapse time: {} sec'.format(time.time() - stime))