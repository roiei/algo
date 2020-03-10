
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False
        
