

class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> int:
        if not nums:
            return 1
        n = len(nums)
        idxs = [False]*n
        for i, num in enumerate(nums):
            if num <= n and num > 0:
                idxs[num-1] = True
        for i, idx in enumerate(idxs):
            if False == idx:
                return i+1
        return n+1


print(Solution().firstMissingPositive([1,2,0]))
