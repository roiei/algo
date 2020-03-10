import time


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: int) -> 'List[int]':
        if not nums:
            return []
        n = len(nums)
        out = []
        for i in range(n-k+1):
            out.append(max(nums[i:i+k]))
        return out


stime = time.time()
print('2 = ', Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7] 
print('elapse time: {} sec'.format(time.time() - stime))

