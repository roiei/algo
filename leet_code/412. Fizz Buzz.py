import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        res = []
        for i in range(1, n + 1):
            val = ''
            if i%3 == 0:
                val += 'Fizz'
            if i%5 == 0:
                val += 'Buzz'
            
            if not val:
                val = str(i)
            
            res += val,
        
        return res


stime = time.time()
print(Solution().nthSuperUglyNumber_mine(12, [2,7,13,19]))
print('elapse time: {} sec'.format(time.time() - stime))