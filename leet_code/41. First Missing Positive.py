import time
from util.util_list import *
from util.util_tree import *
import collections
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        n = len(nums)
        idxs = [False]*n
        for i, num in enumerate(nums):
            if num <= n and num > 0:
                idxs[num-1] = True
        for i, idx in enumerate(idxs):
            if False == idx:
                return i+1
        return n+1

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)

        for i in range(1, n + 1):
            if i not in nums:
                return i

        return i + 1


print(Solution().firstMissingPositive([1,2,0]))
