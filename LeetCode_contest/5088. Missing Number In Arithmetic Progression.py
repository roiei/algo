
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def missingNumber(self, arr: [int]) -> int:
        n = len(arr)
        if n < 1:
            return

        diff = arr[-1] - arr[0]
        diff //= n

        val = arr[0]
        for num in arr:
            if val != num:
                return val
            val += diff

        return diff



stime = time.time()
print(9 == Solution().missingNumber(arr = [5,7,11,13]))
print(14 == Solution().missingNumber(arr = [15,13,12]))
print(0 == Solution().missingNumber([0,0,0,0,0]))

print('elapse time: {} sec'.format(time.time() - stime))