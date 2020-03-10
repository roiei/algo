import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def jump(self, nums: 'List[int]') -> int:
        if not nums:
            return 0
        n = len(nums)
        cache = collections.defaultdict(int)
        
        def dfs(nums, trace, depth, pos, n):
            if not nums:
                return depth
            idx = ''.join([str(n) for n in nums])
            if idx in cache and depth > cache[idx]:
                return cache[idx]
            if n-1 == pos:
                return depth
            if 0 == nums[0]:
                return float('inf')
            subdepth = []
            for i in range(1, nums[0]+1):
                if nums[i:]:
                    subdepth += dfs(nums[i:], [], depth+1, pos+i, n),
            ret = min(subdepth) if subdepth else depth
            cache[idx] = ret
            return ret
    
        depth = dfs(nums, [], 0, 0, len(nums))
        if float('inf') == depth:
            depth = 0
        return depth


    def jump(self, nums):
        if not nums:
            return 0
        n = len(nums)
        minstep = [0]*n
        cur = 0
        start = 0
        while start < n-1:
            if start < cur + nums[cur]:
                until = min(cur+nums[cur], n-1)
                size = 0
                for i in range(start+1, until+1):
                    minstep[i] = minstep[cur] + 1
                    size += 1
                start += size
            cur += 1
        return minstep[-1]


stime = time.time()
print(2 == Solution().jump([2,3,1,1,4]))
print(3 == Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0]))
#print(3 == Solution().jump_ref([2,1,1,1,1]))
print(3 == Solution().jump([2,1,1,1,1]))
#print(3 == Solution().jump_ref([3,4,3,2,5,4,3]))
print(3 == Solution().jump([3,4,3,2,5,4,3]))
print(2 == Solution().jump([4,1,1,3,1,1,1]))
print('elapse time: {} sec'.format(time.time() - stime))