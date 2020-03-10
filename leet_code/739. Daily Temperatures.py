import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        n = len(T)
        res = [0]*n
        stk = [(T[0], 0)]
        for i in range(1, len(T)):
            while stk and stk[-1][0] < T[i]:
                val, idx = stk.pop()
                res[idx] = i-idx
            stk += (T[i], i),
        return res


stime = time.time()
print(Solution().dailyTemperatures_timeout([73, 74, 75, 71, 69, 72, 76, 73]))
print('elapse time: {} sec'.format(time.time() - stime))