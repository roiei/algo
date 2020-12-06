import time


class Solution(object):
    def wiggle(self, nums):
        n = len(nums)
        nums.sort()
        j = 0
        out = []
        for i in range(n//2):
            out.append(nums[i])
            out.append(nums[n-1-i])
        return out


    def wiggle(self, nums):
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n//2):
            res += nums[i],
            res += nums[n - i - 1],

        return res

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
        
        return res


stime = time.time()
print([1, 6, 2, 5, 3, 4] == Solution().wiggle([3, 5, 2, 1, 6, 4])) # 
print('elapse time: {} sec'.format(time.time() - stime))