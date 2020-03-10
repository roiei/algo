
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def numOfSubarrays(self, arr: [int], k: int, threshold: int) -> int:
        n = len(arr)
        if n < k:
            return 0
    
        cnt = 0
        tot = sum(arr[:k - 1])

        for i in range(k - 1, n):
            if i - k >= 0:
                tot -= arr[i - k]
            tot += arr[i]
            avg = tot//k
            if avg >= threshold:
                cnt += 1
        
        return cnt
            

stime = time.time()
print(3 == Solution().numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
print(5 == Solution().numOfSubarrays(arr = [1,1,1,1,1], k = 1, threshold = 0))
print(6 == Solution().numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))
print(1 == Solution().numOfSubarrays(arr = [7,7,7,7,7,7,7], k = 7, threshold = 7))
print(1 == Solution().numOfSubarrays(arr = [4,4,4,4], k = 4, threshold = 1))
print('elapse time: {} sec'.format(time.time() - stime))