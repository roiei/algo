
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        mx = 0
        for account in accounts:
            mx = max(mx, sum(account))
        return mx
        

stime = time.time()
print(6 == Solution().maximumWealth([[1,2,3],[3,2,1]]))
print('elapse time: {} sec'.format(time.time() - stime))