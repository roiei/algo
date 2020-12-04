import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def generateTrees(self, n):
        if not n:
            return []
        memo = {}

        def dfs(nums):
            if nums in memo:
                return memo[nums]

            if not nums:
                memo[nums] = [None]
                return memo[nums]       

            res = []
            for i in range(len(nums)):
                left  = dfs(nums[:i])
                right = dfs(nums[i + 1:])

                for l in left:
                    for r in right:
                        node = TreeNode(nums[i])
                        node.left = l
                        node.right = r
                        res += node,

            memo[nums] = res
            return res

        return dfs(range(1, n + 1))


stime = time.time()
# 3
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
print(Solution().generateTrees(3))
print('elapse time: {} sec'.format(time.time() - stime))