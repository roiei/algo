
import time
from util.util_list import *
from util.util_tree import *
import bisect
import copy
import collections


class Solution:
    def replaceElements(self, arr: [int]) -> [int]:
        if not arr:
            return None
        
        n = len(arr)
        arr = list(zip(arr, [v for v in range(n)]))
        arr.pop(0)        
        arr.sort(key=lambda p: p[0], reverse=True)
        
        res = []

        cur_idx = 0
        for val, idx in arr:

            if cur_idx > idx:
                continue

            while cur_idx < idx:
                res += val,
                cur_idx += 1

            cur_idx = idx

        res += -1,
        return res

    def replaceElements(self, arr: [int]) -> [int]:
        sarr = []
        res = []

        for i in range(len(arr) - 1, -1, -1):
            idx = bisect.bisect_left(sarr, arr[i])
            val = -1 if idx == 0 and not sarr else sarr[-1]
            res.insert(0, val)
            sarr.insert(idx, arr[i])

        return res


stime = time.time()
print([18,6,6,6,1,-1] == Solution().replaceElements(arr = [17,18,5,4,6,1]))
print([60499,60499,57517,26961,-1] == Solution().replaceElements(arr = [56903,18666,60499,57517,26961]))
print('elapse time: {} sec'.format(time.time() - stime))