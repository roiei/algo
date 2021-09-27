import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List
import math
import functools
import heapq


class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        pre = None
        cnt = 0

        for ch in s:
            if ch != pre:
                cnt = 1
                res += ch
            else:
                cnt += 1
                if cnt < 3:
                    res += ch

            pre = ch

        return res


stime = time.time()
print("leetcode" == Solution().makeFancyString(s = "leeetcode"))
print("aabaa" == Solution().makeFancyString(s = "aaabaaaa"))
print("aab" == Solution().makeFancyString(s = "aab"))
print('elapse time: {} sec'.format(time.time() - stime))