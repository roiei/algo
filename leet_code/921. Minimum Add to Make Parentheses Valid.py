
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        
        stk = []
        for ch in S:
            if stk and (stk[-1] == '(' and ch == ')'):
                stk.pop()
                continue
            stk += ch,
        
        return len(stk)


stime = time.time()
print(1 == Solution().minAddToMakeValid("())"))
print(3 == Solution().minAddToMakeValid("((("))
print(0 == Solution().minAddToMakeValid("()"))
print(4 == Solution().minAddToMakeValid("()))(("))
print('elapse time: {} sec'.format(time.time() - stime))