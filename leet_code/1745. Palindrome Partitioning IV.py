import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        seq = []
        
        freq = collections.Counter(s)
        if len(freq) < 3:
            return True
        
        for i in range(len(s)):
            l = r = i
            
            pr = r
            while r + 1 < n and s[r] == s[r + 1]:
                r += 1
            
            while l - 1 >= 0 and r + 1 < n and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            
            while l <= r:
                seq += (l, r + 1),
                l += 1
                r -= 1
        
        seq.sort(key=lambda p: p[0])

        def dfs(seq, start, num_chunks):
            if start == n:
                return num_chunks == 0
                
            if num_chunks == 0:
                return False
            
            for i, val in enumerate(seq):
                l, r = val
                if l != start:
                    continue
                
                if dfs(seq[i + 1:], r, num_chunks - 1):
                    return True
        
            return False
    
        return dfs(seq, 0, 3)


print(True == Solution().checkPartitioning("abcbdd"))
print(False == Solution().checkPartitioning("bcbddxy"))
print(True == Solution().checkPartitioning("bbab"))
print(False == Solution().checkPartitioning("acab"))
print(True == Solution().checkPartitioning("aaa"))