
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def numTimesAllBlue(self, light: [int]) -> int:

        all_idx = 0
        n = len(light)
        bulb = [False]*n
        cnt = 0
        cur_mx = 0

        for i, num in enumerate(light):
            cur_mx = max(cur_mx, num - 1)
            bulb[num - 1] = True

            while all_idx < cur_mx  and bulb[all_idx] == True:
                all_idx += 1

            if all_idx == cur_mx:
                cnt += 1

        return cnt


        
            
            
stime = time.time()
print(3 == Solution().numTimesAllBlue([2,1,3,5,4]))
print(2 == Solution().numTimesAllBlue([3,2,4,1,5]))
print(1 == Solution().numTimesAllBlue([4,1,2,3]))
print(3 == Solution().numTimesAllBlue([2,1,4,3,6,5]))
print(6 == Solution().numTimesAllBlue([1,2,3,4,5,6]))
print('elapse time: {} sec'.format(time.time() - stime))