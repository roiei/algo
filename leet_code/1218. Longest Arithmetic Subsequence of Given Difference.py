import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        n = len(arr)
        dp = [1]*n

        for i in range(n - 1):
            for j in range(i + 1, n):
                if arr[j] - arr[i] == difference:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)


    def longestSubsequence(self, arr, difference):
        idxs = collections.defaultdict(int)
        for num in arr:
            if num - difference in idxs:
                idxs[num] = max(idxs[num], idxs[num - difference] + 1)
            else:
                idxs[num] = 1

        return max(idxs.values())



stime = time.time()
print(24 == Solution().getMaximumGold(grid = [[0,6,0],[5,8,7],[0,9,0]]))
print(28 == Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
print('elapse time: {} sec'.format(time.time() - stime))


