
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def findSpecialInteger(self, arr: [int]) -> int:
        n = len(arr)
        freq = collections.defaultdict(float)
        for num in arr:
            freq[num] += 1
        
        freq = sorted([(k, v/n) for k, v in freq.items()], key=lambda p: p[1], reverse=True)
        return freq[0][0]

            
stime = time.time()
print(6 == Solution().findSpecialInteger([1,2,2,6,6,6,6,7,10]))
print('elapse time: {} sec'.format(time.time() - stime))