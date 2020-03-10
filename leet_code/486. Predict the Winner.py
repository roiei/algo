import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def PredictTheWinner_ref(self, nums: [int]) -> bool:
        cache = {}

        def dfs(nums, l, r, turn):
            nonlocal cache
            if l == r:
                return turn*nums[l]
            if (l, r) in cache:
                return cache[(l, r)]

            val1 = turn*nums[l] + dfs(nums, l+1, r, -turn)
            val2 = turn*nums[r] + dfs(nums, l, r-1, -turn)
            if turn > 0:
                cache[(l, r)] = max(val1, val2)
            else:
                cache[(l, r)] = min(val1, val2)
            return cache[(l, r)]

        res = dfs(nums, 0, len(nums)-1, 1)
        return res >= 0


    def PredictTheWinner(self, nums: [int]) -> bool:
        if not nums:
            return False

        cache = {}
        def dfs(nums, l, r, turn):
            nonlocal cache
            if (l, r) in cache:
                return cache[(l, r)]
            if l == r:
                if True == turn:
                    return nums[l]
                else:
                    return -1*nums[l]

            if True == turn:
                left = nums[l] + dfs(nums, l+1, r, not turn)
                right = nums[r] + dfs(nums, l, r-1, not turn)
                cache[(l, r)] = max(left, right)
            else:
                left = -1*nums[l] + dfs(nums, l+1, r, not turn)
                right = -1*nums[r] + dfs(nums, l, r-1, not turn)
                cache[(l, r)] = min(left, right)
            return cache[(l, r)]

        res = dfs(nums, 0, len(nums)-1, True)
        return res >= 0

    def PredictTheWinner(self, nums: [int]) -> bool:
        if not nums:
            return False

        def dfs(nums, l, r, my_turn):
            if (l, r) in mem:
                return mem[(l, r)]
            if l == r:
                if my_turn == True:
                    return nums[l]
                else:
                    return -1*nums[l]
            if my_turn == True:
                left = nums[l] + dfs(nums, l+1, r, not my_turn)
                right = nums[r] + dfs(nums, l, r-1, not my_turn)
                cur = max(left, right)
            else:
                left = -1*nums[l] + dfs(nums, l+1, r, not my_turn)
                right = -1*nums[r] + dfs(nums, l, r-1, not my_turn)
                cur = min(left, right)
            mem[(l, r)] = cur
            return cur
        mem = {}
        ret = dfs(nums, 0, len(nums)-1, True)
        return True if ret >= 0 else False



stime = time.time()
#print(True == Solution().PredictTheWinner([1, 5, 8, 4]))
# print(False == Solution().PredictTheWinner([1, 5, 2]))
# print(False == Solution().PredictTheWinner_mod([1, 5, 2]))
# print(True == Solution().PredictTheWinner([1, 5, 233, 7]))
# print(True == Solution().PredictTheWinner([1,1]))
# print(True == Solution().PredictTheWinner([0]))
#print(True == Solution().PredictTheWinner([1,2,99]))
print(True == Solution().PredictTheWinner_mod([1,2,99]))
print(True == Solution().PredictTheWinner([1,2,99]))
print('elapse time: {} sec'.format(time.time() - stime))