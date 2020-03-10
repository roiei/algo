
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def sequentialDigits(self, low: int, high: int) -> [int]:
        nums = list(map(int, list(str(low))))
        n = len(nums)
        
        start = []
        for i in range(n - 1):
            if nums[i] + 1 != nums[i + 1]:
                if nums[i] + 1 < nums[i + 1]:
                    start += nums[i] + 1,
                    start += [0]*(n - i - 1)
                else:
                    start += nums[i],
                    start += [0]*(n - i - 1)
                break
            else:
                start += nums[i],

        if len(start) < n:
            start += nums[-1],
        
        q = []
        if start[0] + (n - 1) < 10:
            q += [val for val in range(start[0], start[0] + n)],
        else:
            q += [1] + [val for val in range(2, 2 + n)],
            
        res = []
        while q:
            cur = q.pop(0)
            int_val = int(''.join([str(val) for val in cur]))
            if int_val >= high:
                continue
            res += int_val,
            n = len(cur)
            if cur[0] + 1 + (n - 1) < 10:
                q += [val for val in range(cur[0] + 1, cur[0] + 1 + n)],
            else:
                q += [1] + [val for val in range(2, 2 + n)],

        return res
                
                

stime = time.time()
print([123,234] == Solution().sequentialDigits(low = 100, high = 300))
print([1234,2345,3456,4567,5678,6789,12345] == Solution().sequentialDigits(low = 1000, high = 13000))
#print(Solution().sequentialDigits(low = 234, high = 2314))
print([12345,23456] == Solution().sequentialDigits(low = 8511, high = 23553))
print('elapse time: {} sec'.format(time.time() - stime))