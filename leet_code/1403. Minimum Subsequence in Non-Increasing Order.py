


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        tot = sum(nums)
        nums.sort(reverse=True)
        inc = 0
        res = []
        
        for num in nums:
            inc += num
            res += num,
            if (inc<<1) > tot:
                break
        
        return res