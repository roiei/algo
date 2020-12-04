import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from functools import lru_cache
import functools


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
        

stime = time.time()
print(True == Solution().arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
print('elapse time: {} sec'.format(time.time() - stime))