import time
from typing import List


class Solution(object):
    def wiggleSort(self, nums: List[int]) -> None:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        res = []
        
        offset = 1 if n%2 == 0 else 0
        
        for i in range(n//2):
            res += nums[n//2 - i - offset],
            res += nums[n - i - 1],
        
        if n%2:
            res += nums[0],

        nums[:] = res


stime = time.time()
print([1, 6, 2, 5, 3, 4] == Solution().wiggleSort([3, 5, 2, 1, 6, 4])) # 
print('elapse time: {} sec'.format(time.time() - stime))