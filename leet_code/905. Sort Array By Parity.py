
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        
        for num in A:
            if num%2 == 0:
                even += num,
            else:
                odd += num,
        
        return even + odd    

            
stime = time.time()
print([2,4,3,1] == Solution().sortArrayByParity([3,1,2,4]))
print('elapse time: {} sec'.format(time.time() - stime))