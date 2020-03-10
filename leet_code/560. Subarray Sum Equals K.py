
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        
        cnt = 0
        tot = 0
        idxs = collections.defaultdict(int)
        idxs[0] = 1
        
        for i in range(len(nums)):
            tot += nums[i]
            
            if tot - k in idxs:
                cnt += idxs[tot - k]
            
            idxs[tot] = idxs[tot] + 1
        
        return cnt


stime = time.time()
#print(2 == Solution().subarraySum(nums = [1,1,1], k = 2))
print(4 == Solution().subarraySum(nums = [1,2,1,2,1], k = 3))
print('elapse time: {} sec'.format(time.time() - stime))