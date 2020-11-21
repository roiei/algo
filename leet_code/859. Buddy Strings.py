import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        diff = []
        for a, b in zip(A, B):
            if a != b:
                diff += (a, b),

        if len(diff) > 2 or len(diff) == 1:
            return False

        if len(diff) == 0:
            freq = collections.Counter(A)
            return any([val for val in freq.values() if val > 1])

        return diff[0][::-1] == diff[1]


stime = time.time()
# print(True == Solution().buddyStrings("aa", "aa"))
# print(False == Solution().buddyStrings("ab", "ab"))
print(False == Solution().buddyStrings("ab", "ca"))
# print(True == Solution().buddyStrings("abab", "abab"))
# print(True == Solution().buddyStrings("acccccb", "bccccca"))
# print(False == Solution().buddyStrings("abcaa", "abcbb"))
print('elapse time: {} sec'.format(time.time() - stime))