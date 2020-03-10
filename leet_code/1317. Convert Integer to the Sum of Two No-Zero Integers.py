
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for num in range(1, n):
            if str(num).count('0') == 0 and str(n - num).count('0') == 0:
                return [num, n - num]
        
        return [-1, -1]


            
stime = time.time()
#print([1, 1] == Solution().getNoZeroIntegers(2))
print([1,68] == Solution().getNoZeroIntegers(69))
#print([11,999] == Solution().getNoZeroIntegers(n = 1010))
print('elapse time: {} sec'.format(time.time() - stime))