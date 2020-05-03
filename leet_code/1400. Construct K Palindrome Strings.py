
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq = collections.Counter(s)
        cnt = 0

        if len(s) < k:
            return False
        
        for _, v in freq.items():
            if v%2 != 0:
                cnt += 1
        
        return cnt <= k
        


stime = time.time()
print(True == Solution().canConstruct(s = "annabelle", k = 2))
print(False == Solution().canConstruct(s = "leetcode", k = 3))
print(True == Solution().canConstruct(s = "true", k = 4))
print(True == Solution().canConstruct(s = "yzyzyzyzyzyzyzy", k = 2))
print(False == Solution().canConstruct(s = "cr", k = 7))
print('elapse time: {} sec'.format(time.time() - stime))