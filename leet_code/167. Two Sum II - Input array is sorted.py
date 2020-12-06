import time


class Solution:
    def twoSum(self, numbers, target):
        if not numbers:
            return []
        l = 0
        r = len(numbers)-1
        while l <= r:
            s = numbers[l]+numbers[r]
            if s == target:
                break
            if s > target:
                r -= 1
            else:
                l += 1
        return [l+1, r+1]

    def twoSum(self, nums, target):
        if not nums:
            return []
        
        l = 0
        r = len(nums) - 1

        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            elif s > target:
                r -= 1

        return []


stime = time.time()
# print(Solution().twoSum([2,7,11,15], 9))
# print(Solution().twoSum([2, 3, 4], 6))
# print(Solution().twoSum([-1,0], -1))
# print(Solution().twoSum([0,0,3,4], 0))
print([1, 2] == Solution().twoSum([2,7,11,15], 9))
print('elapse time: {} sec'.format(time.time() - stime))

