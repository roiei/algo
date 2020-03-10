
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        n = len(groupSizes)
        nums = [(i, groupSizes[i]) for i in range(n)]        
        nums.sort(key=lambda p: p[1], reverse=True)
        
        res = []
        
        while nums:
            size = nums[0][1]
            sub = []
            
            while nums and size:
                sub += nums.pop(0)[0],
                size -= 1
            
            res += sub,
        
        return res



stime = time.time()
print(15 == Solution().subtractProductAndSum(n = 234))
print(21 == Solution().subtractProductAndSum(n = 4421))
print('elapse time: {} sec'.format(time.time() - stime))