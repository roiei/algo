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
                res[idx] = i - idx

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

    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        stk = []
        num_days = []

        for i in range(len(temperatures) - 1, -1, -1):
            while stk and stk[-1][0] < temperatures[i]:
                stk.pop()

            if stk:
                num_days += stk[-1][1] - i,
            else:
                num_days += 0,

            stk += (temperatures[i], i),

        return list(reversed(num_days))

    def get_num_days_to_wait(self, temperatures: [int]) -> [int]:
        if not temperatures:
            return []

        n = len(temperatures)
        res = [0]*n
        stk = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            while stk and stk[-1][0] < temperatures[i]:
                val, idx = stk.pop()
                res[idx] = i - idx

            stk += (temperatures[i], i),

        return res


#print(get_num_days_to_wait([65, 68, 67, 75, 70, 69, 72, 74]))

stime = time.time()
print([1, 2, 1, 0, 2, 1, 1, 0] == Solution().dailyTemperatures([65, 68, 67, 75, 70, 69, 72, 74]))
#print([1,1,4,2,1,1,0,0] == Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print('elapse time: {} sec'.format(time.time() - stime))