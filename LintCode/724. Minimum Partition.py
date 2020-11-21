import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution:
    def findMin(self, nums):
        
        tot = sum(nums)
        
        pos = [False]*(tot)
        pos[0] = True
        
        for num in nums:
            for j in range(len(pos) - 1, num - 1, -1):
                pos[j] |= pos[j - num]

        print(pos)
        
        for i in range(len(pos) - 1, -1, -1):
            if pos[i]:
                print(tot, i)
                return abs(tot - i)
        return 0
                       


stime = time.time()
#print(1 == Solution().findMin([1,5,6,11]))
print(20 == Solution().findMin([1,21]))
print('elapse time: {} sec'.format(time.time() - stime))
