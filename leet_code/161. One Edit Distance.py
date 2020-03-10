
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def isOneEditDistance(self, s, t):
        diff = 0
        m = len(s)
        n = len(t)

        if abs(m - n) > 1: 
            return False 

        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
                continue

            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                i += 1
                j += 1

            diff += 1

        if i < m or j < n:
            diff += 1 

        return diff == 1


stime = time.time()
print(True == Solution().isOneEditDistance("aDb", "adb"))
print(True == Solution().isOneEditDistance("abcde", "bcde"))
print('elapse time: {} sec'.format(time.time() - stime))