
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    """
    @param arr: The array you should find shortest subarray length which has duplicate elements.
    @return: Return the shortest subarray length which has duplicate elements.
    """
    def getLength(self, arr):
        idxs = collections.defaultdict(list)
        
        for i, num in enumerate(arr):
            idxs[num] += i,
        
        idxs = [(k, v) for k, v in idxs.items() if len(v) > 1]
        mn = float('inf')
        
        for k, v in idxs:
            for i in range(len(v) - 1):
                mn = min(mn, v[i + 1] - v[i] + 1)
        
        if mn == float('inf'):
            return -1
        return mn


stime = time.time()
print(3 == Solution().getLength([1,2,3,1,4,5,4,6,8]))
print('elapse time: {} sec'.format(time.time() - stime))