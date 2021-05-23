import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)

        s = list(map(lambda p: int(p), s))
        def get_diff_count(start, s):
            flip = start
            ones = zeros = 0
            for i in range(n):
                if flip != s[i]:
                    if 1 == s[i]:
                        ones += 1
                    else:
                        zeros += 1

                flip = 1 if flip == 0 else 0

            return ones == zeros, ones

        mn = float('inf')
        res1, cnt = get_diff_count(1, s)
        if res1:
            mn = min(mn, cnt)
        res2, cnt = get_diff_count(0, s)
        if res2:
            mn = min(mn, cnt)
        if res1 or res2:
            return mn
        return -1



stime = time.time()
#print(1 == Solution().minSwaps("111000"))
#print(0 == Solution().minSwaps("1"))
print(1 == Solution().minSwaps("100"))
print('elapse time: {} sec'.format(time.time() - stime))