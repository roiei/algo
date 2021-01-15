
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
        half = len(s)//2
        def get_num_vowels(str):
            cnt = 0
            for ch in str:
                if ch in 'aeiou':
                    cnt += 1
            return cnt

        return get_num_vowels(s[:half]) == get_num_vowels(s[half:])


stime = time.time()
print(True == Solution().halvesAreAlike("book"))
print(False == Solution().halvesAreAlike("textbook"))
print('elapse time: {} sec'.format(time.time() - stime))