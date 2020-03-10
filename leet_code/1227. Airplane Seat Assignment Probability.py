
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        
        pos = 1.0/n
        
        for i in range(1, n - 1):
            print(pos)
            pos += pos * (1.0/(n - i))
            print(pos)

        return 1 - pos  
   

stime = time.time()
#print(0.50000 == Solution().nthPersonGetsNthSeat(2))
#print(0.50000 == Solution().nthPersonGetsNthSeat(3))
#print(Solution().nthPersonGetsNthSeat(4))
print(Solution().nthPersonGetsNthSeat(5))
print('elapse time: {} sec'.format(time.time() - stime))