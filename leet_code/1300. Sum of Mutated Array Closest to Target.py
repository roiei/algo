
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findBestValue(self, arr: [int], target: int) -> int:
        arr.sort(reverse=True)
        maxA = arr[0]

        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()

        return int((target + len(arr) / 2.0 - 0.1) / len(arr)) if arr else maxA

    def findBestValue(self, arr: [int], target: int) -> int:
        l, r = 0, 10**5
        diff = abs(sum(arr) - target)
        res = collections.defaultdict(list)
        while l < r:
            m = (l + r) // 2
            s = sum([m if n > m else n for n in arr])
            if abs(s - target) <= diff:
                diff = abs(s - target)
                res[diff] += [m]
            if s < target:
                l = m + 1
            else: 
                r = m
        return min(res[diff])
            


stime = time.time()
print([18,6,6,6,1,-1] == Solution().replaceElements(arr = [17,18,5,4,6,1]))
print([60499,60499,57517,26961,-1] == Solution().replaceElements(arr = [56903,18666,60499,57517,26961]))
print('elapse time: {} sec'.format(time.time() - stime))