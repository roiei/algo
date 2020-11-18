import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def dailyTemperatures(self, T: [int]) -> [int]:
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

    def dailyTemperatures(self, T: [int]) -> [int]:
        stk = []
        res = []
        for i in range(len(T) - 1, -1, -1):
            while stk and stk[-1][0] <= T[i]:
                stk.pop()

            if stk:
                idx = stk[-1][1]
                res.insert(0, idx - i)
            else:
                res.insert(0, 0)
            
            stk += (T[i], i),
        
        return res


stime = time.time()
print([1,1,4,2,1,1,0,0] == Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print('elapse time: {} sec'.format(time.time() - stime))