

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0, 1]
        offset = 1
        for i in range(1, n):
            if i%2 == 1:
                nums += nums[offset],
            else:
                nums += nums[offset] + nums[offset + 1],
                offset += 1
                
       
        print(nums) 
        return max(nums)
        

# print(3 == Solution().getMaximumGenerated(7))
# print(1 == Solution().getMaximumGenerated(2))
print(0 == Solution().getMaximumGenerated(0))
        