
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def frequencySort(self, nums: [int]) -> [int]:
        freq = sorted(collections.Counter(nums).items(), key=lambda p: p[1])
        freq_nums = collections.defaultdict(list)
        
        for k, v in freq:
            freq_nums[v] += k,
        
        res = []
        for freq, nums in freq_nums.items():
            nums.sort(reverse=True)
            
            for num in nums:
                res += [num]*freq
        
        return res


stime = time.time()
print([3,1,1,2,2,2] == Solution().frequencySort([1,1,2,2,2,3]))
print('elapse time: {} sec'.format(time.time() - stime))