import time


class Solution(object):
    def nextPermutation(self, nums):
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        for k in range(len(nums) - 1, i - 1, -1):
            if nums[k] > nums[i - 1]:
                break

        nums[i - 1], nums[k] = nums[k], nums[i - 1]
        nums[i:] = nums[i:][::-1]

        return nums


nums = [1,2,3] # 1, 3, 2
#nums = [3,2,1] # 1, 2, 3
#nums = [1,1,5] # 1, 5, 1
nums = [1,3,2] # 2, 1, 3
nums = [1,5,1] # 5, 1, 1

stime = time.time()
#print(Solution().nextPermutation([2,2,3,4,2,3,1,1,2]))
print([1, 3, 2, 4] == Solution().nextPermutation([1, 2, 4, 3]))
print('elapse time: {} sec'.format(time.time() - stime))


