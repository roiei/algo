import time


class Solution:
    def moveZeroes(self, nums: 'List[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        num_zeros = nums.count(0)
        for i in range(num_zeros):
            nums.append(nums.pop(nums.index(0)))

    def moveZeroes(self, nums: [int]) -> None:
        n = len(nums)
        l = 0
        zeros = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            
            nums[l] = num
            
            if num != 0:
                l += 1

        for i in range(n - zeros, n):
            nums[i] = 0

    def moveZeroes(self, nums: [int]) -> None:
        n = len(nums)
        widx = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[widx] = nums[i]
                widx += 1
        
        for i in range(widx, n):
            nums[i] = 0
        

stime = time.time()
sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))
print('elapse time: {} sec'.format(time.time() - stime))