import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == m else False
            
            
stime = time.time()
print(Solution().isSubsequence("abc", "ahbgdc"))
print('elapse time: {} sec'.format(time.time() - stime))

     