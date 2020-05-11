
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def longestSubarray(self, nums: [int], limit: int) -> int:
        seq_ordered = []
        seq = []
        l = r = 0
        mx = 0
        
        while r < len(nums):
            idx = bisect.bisect_left(seq_ordered, nums[r])
            seq_ordered.insert(idx, nums[r])
            seq += nums[r],

            while seq_ordered and seq_ordered[-1] - seq_ordered[0] > limit:
                idx = seq_ordered.index(seq.pop(0))
                seq_ordered.pop(idx)
                l += 1

            mx = max(mx, r - l + 1)
            r += 1
    
        return mx
        

stime = time.time()
print(4  == Solution().longestSubarray(nums = [10,1,2,4,7,2], limit = 5))
print('elapse time: {} sec'.format(time.time() - stime))