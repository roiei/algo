import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stk = []
        for val in preorder.split(','):
            stk += val,
            while len(stk) >= 2 and stk[-2] == '#' and stk[-1] == '#':
                stk.pop()
                stk.pop()
                if not stk:
                    return False
                stk.pop()
                stk += '#',
        return stk == ['#']


stime = time.time()
print(True == Solution().isValidSerialization([2,-1,1,2,2]))
print('elapse time: {} sec'.format(time.time() - stime))