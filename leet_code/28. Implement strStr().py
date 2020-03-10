import time
from util_list import *


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if '' == haystack:
            if '' != needle:
                return -1
            return 0
        if haystack == needle:
            return 0
        n = len(haystack)
        m = len(needle)
        for i in range(n-m+1):
            found = True
            for j in range(m):
                if haystack[i+j] != needle[j]:
                    found = False
            if True == found:
                return i
        return -1


stime = time.time()
print(Solution().strStr("hello", 'll'))
print(Solution().strStr("mississippi", 'a'))
print(Solution().strStr("mississippi", 'pi'))
print('elapse time: {} sec'.format(time.time() - stime))
