
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def getWinner(self, arr: [int], k: int) -> int:
        cur = arr[0]
        cnt = 0

        for i in range(1, len(arr)):
            if cur < arr[i]:
                cur = arr[i]
                cnt = 1

            if cnt == k:
                return cur

            cnt += 1
    
        return cur
            
            
stime = time.time()
print(99 == Solution().getWinner([1,11,22,33,44,55,66,77,88,99], 1000000000))
print(5 == Solution().getWinner(arr = [2,1,3,5,4,6,7], k = 2))
print(3 == Solution().getWinner(arr = [3,2,1], k = 10))
print(9 == Solution().getWinner(arr = [1,9,8,2,3,7,6,4,5], k = 7))
print('elapse time: {} sec'.format(time.time() - stime))