import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def handle_backspace(s):
            stk = []
            for ch in s:
                if '#' == ch and stk:
                    stk.pop()
                elif '#' != ch:
                    stk += ch,
            return stk
        if handle_backspace(list(S)) == handle_backspace(list(T)):
            return True
        return False


stime = time.time()
print(Solution().backspaceCompare("y#fo##f", "y#f#o##f"))
print('elapse time: {} sec'.format(time.time() - stime))