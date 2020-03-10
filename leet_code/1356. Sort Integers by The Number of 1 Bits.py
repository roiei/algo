
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        bits = collections.defaultdict(list)
        for num in arr:
            bnum = '{:b}'.format(num)
            ones = bnum.count('1')
            bits[ones] += num,
        
        res = []
        keys = sorted(bits.keys(), reverse=False)
        for key in keys:
            res += sorted(bits[key])
        
        return res
        
            
stime = time.time()
print([0,1,2,4,8,3,5,6,7] == Solution().sortByBits([0,1,2,3,4,5,6,7,8]))
print('elapse time: {} sec'.format(time.time() - stime))