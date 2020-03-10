import time
from util_list import *
from util_tree import *


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        n = len(s)
        for i in range(1, n//2+1):
            if s == s[:i]*(n//i):
                return True
        return False



stime = time.time()
print(Solution().repeatedSubstringPattern("abab"))
print(Solution().repeatedSubstringPattern("aba"))
print(Solution().repeatedSubstringPattern("abcabcabcabc"))
print('elapse time: {} sec'.format(time.time() - stime))

