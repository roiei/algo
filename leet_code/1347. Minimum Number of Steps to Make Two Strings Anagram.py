
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = collections.Counter(s)
        t = collections.Counter(t)

        diff = collections.defaultdict(int) #s - t
        for k in s:
            if k not in t:
                diff[k] = s[k]
            else:
                diff[k] = abs(s[k] - t[k])

        for k in t:
            if k not in s:
                diff[k] = t[k]
            elif diff[k] == 0:
                diff[k] = abs(s[k] - s[k])

        return sum([v for k, v in diff.items() if v != 0])//2

            
stime = time.time()
#print(1 == Solution().minSteps(s = "bab", t = "aba"))
print(5 == Solution().minSteps(s = "leetcode", t = "practice"))
# print(0 == Solution().minSteps(s = "anagram", t = "mangaar"))
# print(0 == Solution().minSteps(s = "xxyyzz", t = "xxyyzz"))
# print(4 == Solution().minSteps(s = "friend", t = "family"))
print('elapse time: {} sec'.format(time.time() - stime))