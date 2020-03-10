
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def findClosestElements(self, arr: [int], k: int, x: int) -> [int]:
        n = len(arr)
        if x <= arr[0]:
            return arr[:k]
        elif arr[n - 1] <= x:
            return arr[n - k:n]

        idx = bisect.bisect_left(arr, x)
        low = 0                 # max(0, idx - k - 1)
        high = len(arr) - 1     # min(len(arr) - 1, idx + k - 1)

        while high - low + 1 > k:
            #if x - arr[low] <= arr[high] - x:
            if x - arr[low] <= arr[high] - x:
            #if x <= arr[high] + arr[low] - x:
                high -= 1
            elif 2*x > arr[high] + arr[low]:
                low += 1

        return arr[low:high + 1]
   

stime = time.time()
print([3,3,4] == Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))
print('elapse time: {} sec'.format(time.time() - stime))