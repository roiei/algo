class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num
