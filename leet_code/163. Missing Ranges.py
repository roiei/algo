
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        nums = set(nums)
        nums = sorted([num for num in nums if lower <= num <= upper])

        def get_range_str(start, end):
            res = ''
            if start == end:
                res = '{}'.format(start)
            else:
                res = '{}->{}'.format(start, end)
            return res


        end = start = cur = lower
        res = []

        for i in range(len(nums)):
            if cur != nums[i]:
                res += get_range_str(cur, nums[i] - 1),
                cur = nums[i]

            cur += 1

        if cur - 1 != upper:
            res += get_range_str(cur, upper),

        if cur == upper and not res:
            res += str(cur),

        return res







stime = time.time()
#print(["2", "4->49", "51->74", "76->99"] == Solution().findMissingRanges(nums = [0, 1, 3, 50, 75], lower = 0, upper = 99))
#print(["1"] == Solution().findMissingRanges([], 1, 1))
#print([] == Solution().findMissingRanges([1,2,3,4,5,6,7,8], 1, 8))
print(["-2147483647->-1","1->2147483646"] == Solution().findMissingRanges([-2147483648,-2147483648,0,2147483647,2147483647], 
-2147483648, 2147483647))
print('elapse time: {} sec'.format(time.time() - stime))