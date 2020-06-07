
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0

        cur = s[0]
        mx = cnt = 1
        for i in range(1, len(s)):
            if s[i] == cur:
                cnt += 1
                mx = max(cnt, mx)
                continue

            cnt = 1
            cur = s[i]

        return mx


stime = time.time()
print(2 == Solution().maxPower(s = "leetcode"))
print('elapse time: {} sec'.format(time.time() - stime))