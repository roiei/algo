
class Solution:
    def missingNumber(self, nums: 'List[int]') -> int:
        if not nums:
            return 1
        n = len(nums)
        idxs = [False]*n
        for i, num in enumerate(nums):
            if num < n and num >= 0:
                idxs[num] = True
        for i, idx in enumerate(idxs):
            if False == idx:
                return i
        return n

    def missingNumber(self, nums):
        n = len(nums)
        nums = set(nums)
        
        for i in range(n + 1):
            if i not in nums:
                return i
        return -1
    
    
    def missingNumber(self, nums):
        n = len(nums)
        for i, num in enumerate(nums):
            n ^= i ^ num
        return n
    
    
    def missingNumber(self, nums):
        n = len(nums)
        triangle = n*(n + 1)//2        
        return triangle - sum(nums)

    


print(Solution().missingNumber([3,0,1]))
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
print(Solution().missingNumber([1]))
