
import time
import copy
import collections


class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        mx = 0
        
        for i in range(1, n):
            if s[:i] == s[n - i:]:
                mx = max(mx, i)
    
        return s[:mx]


stime = time.time()
print("l" == Solution().longestPrefix("level"))
print("abab" == Solution().longestPrefix("ababab"))
print("leet" == Solution().longestPrefix("leetcodeleet"))
print("aaaa" == Solution().longestPrefix("aaaaa"))
print("" == Solution().longestPrefix("a"))
print('elapse time: {} sec'.format(time.time() - stime))