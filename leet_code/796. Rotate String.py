import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if '' == A and '' == B:
            return True
        if ('' == A and '' != B) or ('' == B and '' != A):
            return False
        a = list(A)
        b = list(B)
        for i in range(len(a)):
            if a == b:
                return True
            a += a.pop(0),
        return False


stime = time.time()
print(True == Solution().rotateString('abcde', 'cdeab'))
print('elapse time: {} sec'.format(time.time() - stime))