
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def maxDotProduct(self, nums1: [int], nums2: [int]) -> int:
        m = len(nums1)
        n = len(nums2)

        dp = [[0]*(m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i - 1][j - 1] + nums1[j - 1]*nums2[i - 1],
                    dp[i][j - 1])

                print(dp)

        res = dp[n][m]
        if dp[n][m] == 0:
            res = max(max(nums1)*max(nums2),
                max(nums1)*min(nums2),
                min(nums1)*max(nums2),
                min(nums1)*min(nums2))

        return res


    def maxDotProduct(self, nums1: [int], nums2: [int]) -> int:
        m = len(nums1)
        n = len(nums2)

        def dfs(l, r):
            if l == m or r == n:
                return 0

            res = []
            res += nums1[l]*nums2[r] + dfs(l + 1, r + 1),
            if l + 1 <= m:
                res += dfs(l + 1, r),
            if r + 1 <= n:
                res += dfs(l, r + 1),

            return max(res)

        res = dfs(0, 0)
        print(res)
        return res
    

    def maxDotProduct(self, nums1: [int], nums2: [int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0]*(m) for _ in range(n)]

        for i in range(n):
            for j in range(m):
                dp[i][j] = nums1[i]*nums2[j]

                if i and j:
                    dp[i][j] += max(dp[i - 1][j - 1], 0)

                if i:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])

                if j:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])

        return dp[-1][-1]


stime = time.time()
# print(18 == Solution().maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6]))
# print(21 == Solution().maxDotProduct([3,-2], [2,-6,7]))
print(-1 == Solution().maxDotProduct([-1,-1], [1,1]))
#print(-3 == Solution().maxDotProduct([-5,-1,-2], [3,3,5,5]))
#print(28 == Solution().maxDotProduct([5,-4,-3], [-4,-3,0,-4,2]))
print('elapse time: {} sec'.format(time.time() - stime))