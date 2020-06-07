
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def smallestRepunitDivByK(self, K):
        if K%2 == 0 or K%5 == 0:
            return -1
        if K == 1:
            return 1
        
        count, N = 1, 1

        
        
        while N%K > 0:
            N = (N%K)*10 + 1
            print(N)
            count += 1
        
        return count


stime = time.time()
print(6 == Solution().smallestRepunitDivByK(7))
#print(4 == Solution().characterReplacement(s = "AABABBA", k = 1))
print('elapse time: {} sec'.format(time.time() - stime))

