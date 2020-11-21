
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache
import bisect


"""
1 -> 5
2 -> 15  (10)
3 -> 35  (20)
4 -> 70  (35)
5 -> 126 (56)
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        aset = set(list('aeiou'))
        for i in range(1, n):
            new_aset = set()
            for val in list(aset):
                for ch in 'aeiou':
                    new_aset.add(''.join(sorted(val + ch)))
            aset = new_aset

        return len(aset)


stime = time.time()
print(15 == Solution().countVowelStrings(2))
print(35 == Solution().countVowelStrings(3))
print(70 == Solution().countVowelStrings(4))
print(126 == Solution().countVowelStrings(5))
#print(66045 == Solution().countVowelStrings(33))
print('elapse time: {} sec'.format(time.time() - stime))
