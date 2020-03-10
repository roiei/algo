
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
import heapq


class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        res = []

        mtbl = {}        
        for i in range(1, 10):
            mtbl[str(i)] = chr(ord('a') + i - 1)

        for i in range(10, 27):
            mtbl[str(i) + '#'] = chr(ord('j') + i - 10)

        i = n - 1
        while i >= 0:
            if s[i] == '#':
                res += mtbl[s[i - 2] + s[i - 1] + s[i]],
                i -= 3
            else:
                res += mtbl[s[i]],
                i -= 1

        return ''.join(res[::-1])


stime = time.time()
print("jkab" == Solution().freqAlphabets("10#11#12"))
print("acz" == Solution().freqAlphabets("1326#"))
print('elapse time: {} sec'.format(time.time() - stime))