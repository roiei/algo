
import time

class Solution:
    def findErrorNums(self, nums: 'List[int]') -> 'List[int]':
        nums.sort()
        l = len(nums)
        dup = missing = 0
        prev = 0
        for i in range(1, l+1):
            if prev == nums[i-1]:
                dup = nums[i-1]
            prev = nums[i-1]
        nums.remove(dup)
        nums[len(nums):] = [0]
        for i in range(1, len(nums)+1):
            if i != nums[i-1]:
                missing = i
                break
        return [dup, missing]


        


stime = time.time()
sol = Solution()
print(sol.findErrorNums([1,2,2,4])) # [2, 3]
print(sol.findErrorNums([1,1])) # [1, 2]
print(sol.findErrorNums([2, 2])) # [2, 1]
print(sol.findErrorNums([3, 2, 2])) # [2, 1]
print(sol.findErrorNums([3,2,3,4,6,5])) # [3, 1]
print(sol.findErrorNums([1,5,3,2,2,7,6,4,8,9])) # [2, 10]
print('elapse time: {} sec'.format(time.time() - stime))
