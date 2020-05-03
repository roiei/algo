
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


# var minMoves = function(nums) {
#     var cnt = 0
#     var mn = Math.min(...nums)
    
#     for (var i = 0; i < nums.length; i++) {
#         cnt += Math.abs(nums[i] - mn)
#     }
    
#     return cnt
# };



class Solution:
    def minMoves(self, nums: List[int]) -> int:
        cnt = 0
        mn = min(nums)
        
        for num in nums:
            cnt += abs(num - mn)
        
        return cnt


stime = time.time()
print('elapse time: {} sec'.format(time.time() - stime))