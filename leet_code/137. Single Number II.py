class Solution:
    def singleNumber(self, nums: 'List[int]'):
        if not nums:
            return 0
        return (sum(set(nums))*3 - sum(nums))//2


print(Solution().singleNumber([2,2,3,2]))