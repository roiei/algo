
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        mx = cnt = 0
        for i in range(min(n, k)):
            if s[i] in 'aeiou':
                cnt += 1
        
        mx = max(mx, cnt)
        
        for i in range(min(n, k), n):
            if s[i - k] in 'aeiou':
                cnt -= 1
            if s[i] in 'aeiou':
                cnt += 1
            
            mx = max(mx, cnt)
        
        return mx

                


stime = time.time()
print(3 == Solution().maxVowels(s = "abciiidef", k = 3))
print('elapse time: {} sec'.format(time.time() - stime))