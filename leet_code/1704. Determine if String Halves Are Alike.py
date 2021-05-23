
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache
from typing import List
import bisect


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        
        def count_vowels(s):
            cnt = 0
            for ch in s:
                if ch in 'aeiou':
                    cnt += 1
            return cnt
    
        return count_vowels(s[:n//2]) == count_vowels(s[n//2:])


stime = time.time()
print(True == Solution().halvesAreAlike("book"))
print(False == Solution().halvesAreAlike("textbook"))
print('elapse time: {} sec'.format(time.time() - stime))