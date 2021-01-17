import time
from util.util_list import *
from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        right = [0]
        left = [0]
        
        for i in range(1, len(nums)):
            right += abs(nums[i - 1] - nums[i]),
            left.insert(0, abs(nums[len(nums) - 1 - i] - nums[len(nums) - i]))
        
        res = []
        for i in range(len(nums)):
            tot = 0
            mul = i
            for j in range(i - 1, -1, -1):
                tot += left[j]*mul
                mul -= 1
            
            mul = len(nums) - 1 - i
            for j in range(i + 1, len(nums)):
                tot += right[j]*mul
                mul -= 1
            
            res += tot,
        
        return res

    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        left = [0, nums[0]]
        right = [nums[-1], 0]

        for i in range(1, n):
            cur = nums[i] + left[-1]
            left += cur,

        for i in range(n - 2, -1, -1):
            cur = nums[i] + right[0]
            right.insert(0,cur)

        print(left)
        print(right)

        for i in range(n):
            numleft = i
            numright = n - i - 1

            print(i, nums[i], numleft, left[i], right[i + 1], numright)
            t = nums[i] * numleft - left[i] + right[i+1] - nums[i] * numright
            res += t,

        return res
                

stime = time.time()
print([4,3,5] == Solution().getSumAbsoluteDifferences([2,3,5]))
print('elapse time: {} sec'.format(time.time() - stime))
