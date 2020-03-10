
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def minCut(self, s: str) -> int:
        dp = [0]*len(s)
        
        for i in range(len(s) - 2, -1, -1):
            if s[i:] == s[i:][::-1]:
                dp[i] = 0
                continue

            tmp = []
            for j in range(i + 1, len(s)):
                if s[i:j] == s[i:j][::-1]:
                    tmp += dp[j],
            dp[i] = 1 + min(tmp)
            
        return dp[0]
    


stime = time.time()
print(1 == Solution().minCut("aab"))    # ["aa","b"] could be produced using 1 cut
print('elapse time: {} sec'.format(time.time() - stime))