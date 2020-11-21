
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False


    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            False
        
        nums.sort()
        pre = None
        
        for i in range(len(nums)):
            if nums[i] == pre:
                return True
            pre = nums[i]
            
        return False
        
