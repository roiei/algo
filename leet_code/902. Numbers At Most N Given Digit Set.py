import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from functools import lru_cache
import functools


class Solution:
    def atMostNGivenDigitSet(self, digits: [str], n: int) -> int:
        @functools.lru_cache
        def dfs(tot):
            if int(tot) > n:
                return 0
            
            res = 0
            for digit in digits:
                res += dfs(tot + digit)
            return res + 1
    
        return dfs('0') - 1
        


stime = time.time()
#print(20 == Solution().atMostNGivenDigitSet(["1","3","5","7"], n = 100))
#print(29523 == Solution().atMostNGivenDigitSet(["1","4","9"], n = 1000000000))
print(1222386 == Solution().atMostNGivenDigitSet(["1","3","5","6","7","8"], 62774961))
print('elapse time: {} sec'.format(time.time() - stime))