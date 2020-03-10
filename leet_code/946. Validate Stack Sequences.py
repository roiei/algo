import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:
        n = len(pushed)
        m = len(popped)
        if n != m:
            return False

        i = j = 0
        res, stk = [], []
        while i < n or j < m:
            stk += pushed[i],
            i += 1
            while stk and stk[-1] == popped[j]:
                res += stk.pop(),
                j += 1

        if res == popped:
            return True
        return False


    def validateStackSequences2(self, pushed: [int], popped: [int]) -> bool:
        stk, j = [], 0
        trace = []
        for i in range(len(pushed)):
            stk += pushed[i],
            while stk and stk[-1] == popped[j]:
                trace += stk.pop(),
                j += 1
        return not stk

            

stime = time.time()
# print(Solution().validateStackSequences([1, 0], [1, 0]))
print(Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
# print(Solution().validateStackSequences([0, 2, 1], [0, 1, 2]))
# print(Solution().validateStackSequences([2,1,0], [1,2,0]))
# print(Solution().validateStackSequences([1,3,2,0], [1,2,0,3]))
# print(Solution().validateStackSequences([2,3,0,1], [0,3,2,1]))
print('elapse time: {} sec'.format(time.time() - stime))