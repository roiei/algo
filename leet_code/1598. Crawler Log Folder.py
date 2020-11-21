import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []

        for log in logs:
            if log == '../':
                if stk:
                    stk.pop()
                continue
            elif log == './':
                continue

            stk += log,

        return len(stk)
            

stime = time.time()
print(3 == Solution().minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"]
))
print('elapse time: {} sec'.format(time.time() - stime))