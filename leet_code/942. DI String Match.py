import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)
        cnt = 0
        bcnt = n
        out = []
        for i in range(n):
            if S[i] == 'I':
                out += cnt,
                cnt += 1
            elif S[i] == 'D':
                out += bcnt,
                bcnt -= 1
        out += cnt,
        return out


stime = time.time()
print([0,4,1,3,2] == Solution().diStringMatch("IDID"))
print('elapse time: {} sec'.format(time.time() - stime))