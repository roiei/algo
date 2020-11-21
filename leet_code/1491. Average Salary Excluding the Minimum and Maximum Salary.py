import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def average(self, salary: [int]) -> float:
        mnidx = salary.index(min(salary))
        mxidx = salary.index(max(salary))
        salary.pop(mnidx)
        if mnidx != mxidx:
            salary.pop(salary.index(max(salary)))

        return sum(salary)/len(salary)


stime = time.time()
#print(2500.00000 == Solution().average(salary = [4000,3000,1000,2000]))
print(2000.00000 == Solution().average(salary = [1000,2000,3000]))
print('elapse time: {} sec'.format(time.time() - stime))

