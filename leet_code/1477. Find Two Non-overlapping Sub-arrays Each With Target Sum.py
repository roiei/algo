import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def minSumOfLengths(self, arr: [int], target: int) -> int:
        idxs = collections.defaultdict(int)
        idxs[0] = -1
        inc = 0
        q = []
        
        for i, num in enumerate(arr):
            inc += num
            idxs[inc] = i
            diff = inc - target
            if diff in idxs:
                heapq.heappush(q, (idxs[inc] - idxs[diff], i))

        while len(q) > 1:
            len1, end1 = heapq.heappop(q)
            len2, end2 = heapq.heappop(q)
            if end1 <= end2 - len2 or end2 <= end1 - len1:    
                return len1 + len2
            else:
                heapq.heappush(q, (len1, end1))

        return -1


stime = time.time()
#print(2 == Solution().minSumOfLengths([3,2,2,4,3], 3))
#print(-1 == Solution().minSumOfLengths([4,3,2,6,2,3,4], 6))
print(3 == Solution().minSumOfLengths([1, 0, 6, 1, 7], 7))
#print(Solution().minSumOfLengths([1,2,3,3,3], 6))
print('elapse time: {} sec'.format(time.time() - stime))