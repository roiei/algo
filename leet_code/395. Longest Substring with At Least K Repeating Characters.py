
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        counter = collections.Counter(s)
        char, num = min(counter.items(),key=lambda item: item[1])             
        if num >= k: 
            return len(s)
         
        invalid_idx = s.find(char)
        left  = s[0:invalid_idx]
        right = s[invalid_idx+1:]
        return max(self.longestSubstring(left, k), self.longestSubstring(right, k))

    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(s):
            if not s:
                return 0

            freq = collections.Counter(s)
            ch, v = min(freq.items(), key=lambda p: p[1])
            if v >= k:
                return len(s)

            idx = s.find(ch)
            return max(dfs(s[:idx]), dfs(s[idx + 1:]))

        return dfs(s)



stime = time.time()
print(5 == Solution().longestSubstring(s = "ababbc", k = 2))
print('elapse time: {} sec'.format(time.time() - stime))

