
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        idxs = collections.defaultdict(int)
        idxs[0] = -1
        tot = 0
        
        for i, num in enumerate(nums):
            tot += num
            if k:
                tot %= k
            
            if tot in idxs:
                if i - idxs[tot] > 1:
                    return True
                continue
            
            idxs[tot] = i
        
        return False


stime = time.time()
#print(True == Solution().checkSubarraySum([23, 2, 6, 4, 7],  k=6))
print(False == Solution().checkSubarraySum([1,0], 2))
print('elapse time: {} sec'.format(time.time() - stime))