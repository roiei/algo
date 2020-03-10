
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def smallestDivisor(self, nums: [int], threshold: int) -> int:
        
        l = 1
        r = max(nums)
        m = (l + r)//2
        
        while l < r:
            m = (l + r)//2
            
            tot = 0
            for num in nums:
                quotient = num//m

                if num % m:
                    quotient += 1
                
                tot += quotient
            
            if tot <= threshold:
                r = m
            else:
                l = m + 1

        return l


stime = time.time()
print(5 == Solution().smallestDivisor([1,2,5,9], 6))
print(4 == Solution().smallestDivisor([19], 5))
print('elapse time: {} sec'.format(time.time() - stime))