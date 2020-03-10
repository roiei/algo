
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    # timeout at last
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        mx = start = end = 0
        
        for i in range((n + 1)//2):
            l = i
            r = i
            while r + 1 < n and s[i] == s[r + 1]:
                r += 1
            
            while l > 0 and r + 1 < n and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            
            if l == 0 and mx < r - l + 1:
                mx = max(mx, r - l + 1)
                start = l
                end = r
    
        return s[mx:][::-1] + s


stime = time.time()
#print("aba" == Solution().shortestPalindrome("aba"))
print("dcabbacd" == Solution().shortestPalindrome("abbacd"))
print('elapse time: {} sec'.format(time.time() - stime))