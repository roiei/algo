import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if (not A and B) or (A and not B):
            return False
        if not A and not B:
            return False
        A = list(A)
        B = list(B)
        diff = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff += (A[i], B[i]),
        if len(diff) > 2:
            return False
        if len(diff) == 0:
            A.sort()
            B.sort()
            pre = A[0]
            for i in range(1, len(A)):
                if pre == A[i]:
                    return True
                pre = A[i]
            return False
        return True if diff[0][::-1] == diff[1] else False
           


stime = time.time()
#print(True == Solution().buddyStrings("aa", "aa"))
#print(False == Solution().buddyStrings("ab", "ab"))
#print(True == Solution().buddyStrings("abab", "abab"))
print(True == Solution().buddyStrings("acccccb", "bccccca"))
print('elapse time: {} sec'.format(time.time() - stime))