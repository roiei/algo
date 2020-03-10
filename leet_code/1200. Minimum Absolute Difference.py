import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        res = []
        
        min_diff = float('inf')
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) < min_diff:
                min_diff = abs(arr[i] - arr[i - 1])
        
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) == min_diff:
                res += (arr[i - 1], arr[i]),
        
        return res


stime = time.time()
print([[1,2],[2,3],[3,4]] == Solution().minimumAbsDifference([4,2,1,3]))
print('elapse time: {} sec'.format(time.time() - stime))


