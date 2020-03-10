
from functools import reduce
#import numpy  #res.append(numpy.prod(nums))

class Solution:
    def productExceptSelf1(self, nums: 'List[int]') -> 'List[int]':
        res = []
        for i in range(len(nums)):
            keep = nums[i]
            nums[i] = 1
            res.append(reduce((lambda p1, p2: p1*p2), nums))
            nums[i] = keep
        return res

    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        n = len(nums)
        res = [1 for i in range(n)]
        for i in range(1, n):
            res[i] = res[i-1]*nums[i-1]
        rp = 1
        for i in range(n-1, -1, -1):
            res[i] *= rp
            rp *= nums[i]
        return res

nums = [1,2,3,4]

sol = Solution()
ret = sol.productExceptSelf(nums)
print(ret)