
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def minTaps(self, n: int, ranges: [int]) -> int:
        dp = [0] + [n + 2] * n
        for i, x in enumerate(ranges):
            for j in range(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
        return dp[n] if dp[n] < n + 2 else -1


    def minTaps(self, n: int, ranges: [int]) -> int:
        scopes = sorted([[i - r, i + r] for i, r in enumerate(ranges)], key=lambda p: p[0])

        print(scopes)

        new_scopes = []
        for scope in scopes:
            if (scope[0] < 0 and scope[1] < 0):
                continue

            if scope[0] >= n and scope[1] >= n:
                continue

            if scope[0] < 0:
                new_scopes += [0, scope[1]],
            elif scope[1] > n:
                new_scopes += [scope[0], n],
            else:
                new_scopes += scope,

        scopes = new_scopes

        print(scopes)

        cur = [scopes[0]]

        for scope in scopes:
            if cur[-1][0] >= scope[0] and cur[-1][1] <= scope[1]:
                cur[-1][0] = scope[0]
                cur[-1][1] = scope[1]
            elif cur[-1][1] < scope[1]:
                cur += scope,

        print(cur)
        i = 0
        res = len(cur)
        while i < len(cur) - 1:
            if cur[i][1] >= cur[i + 1][0]:
                cur[i][1] = cur[i + 1][1]
                cur.pop(i + 1)
            else:
                i += 1

        print(cur)
        return res if cur[-1][0] <= 0 and cur[-1][1] >= n else -1


    def minTaps(self, n: int, ranges: List[int]) -> int:
        scopes = sorted([[i - r, i + r] for i, r in enumerate(ranges)], key=lambda p: p[0])
        pre_s = scopes[0][0] - 1
        pre_e = 0                   # range must start from 0
        cnt = 0

        for s, e in scopes:
            if pre_e >= n or pre_e < s:
                break

            if pre_s < s <= pre_e:
                pre_s = pre_e
                cnt += 1

            pre_e = max(pre_e, e)

        return cnt if cnt and pre_e >= n else -1


       

stime = time.time()
print(1 == Solution().minTaps(n = 5, ranges = [3,4,1,1,0,0]))
print(3 == Solution().minTaps(n = 7, ranges = [1,2,1,0,2,1,0,1]))
print(1 == Solution().minTaps(8, [4,0,0,0,4,0,0,0,4]))
print(2 == Solution().minTaps(9, [0,5,0,3,3,3,1,4,0,4]))
print('elapse time: {} sec'.format(time.time() - stime))