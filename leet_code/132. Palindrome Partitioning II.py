
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        dp[0] = 1

        for end in range(1, n):
            mns = []
            for start in range(0, end):
                if s[start:end + 1] == s[start:end + 1][::-1]:
                    if start > 0:
                        mns += dp[start - 1],
                    else:
                        mns += 0,
                else:
                    dp[end] = dp[end - 1] + 1


            if mns:
                dp[end] = min(mns) + 1

            print(dp)
            print()

        return dp[-1] - 1


        
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
print(Solution().minCut("abcbd"))
#print(Solution().minCut("ccbcbd"))
#print(1 == Solution().minCut("aab"))    # ["aa","b"] could be produced using 1 cut
print('elapse time: {} sec'.format(time.time() - stime))