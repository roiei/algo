import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if not arr:
            return True
    
        if len(arr) < 2:
            return True

        arr.sort()
        diff = arr[0] - arr[1]
        
        for i in range(1, len(arr) - 1):
            if diff != arr[i] - arr[i + 1]:
                return False
    
        return True




stime = time.time()
print(True == Solution().canMakeArithmeticProgression(arr = [3,5,1]))
print('elapse time: {} sec'.format(time.time() - stime))

