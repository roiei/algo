# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

# Return the maximum length of a subarray with positive product.


# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.


#     1  -2  -3  4

#     1    -2  -3  4         1 -2 -3      4


import time
from operator import mul
from functools import reduce


class Solution:
    def getMaxLen(self, nums: [int]) -> int:
        mx_len = 0
        pos = neg = 0

        for num in nums:
            if num > 0:
                if neg != 0:
                    neg += 1
                pos += 1
            elif num < 0:
                if neg == 0:
                    neg = pos
                    pos = 0
                else:
                    pos, neg = neg, pos
                    pos += 1

                neg += 1
            else:
                pos = 0
                neg = 0

            #print(num, '-->', neg, pos)
            mx_len = max(mx_len, pos)
        return mx_len


stime = time.time()
#print(4 == Solution().getMaxLen(nums = [1,-2,-3,4]))
print(3 == Solution().getMaxLen(nums = [0,1,-2,-3,-4]))
print('elapse time: {} sec'.format(time.time() - stime))

        