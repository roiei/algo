import time
from util.util_list import *


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

    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        i = j = 0

        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1


stime = time.time()
print(0 == Solution().strStr("", ''))
# print(Solution().strStr("hello", 'll'))
# print(Solution().strStr("mississippi", 'a'))
# print(Solution().strStr("mississippi", 'pi'))
print('elapse time: {} sec'.format(time.time() - stime))
