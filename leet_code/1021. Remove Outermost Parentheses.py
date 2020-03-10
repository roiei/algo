
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        level = 0
        res = []
        
        for ch in S:
            if level == 0 and ch == '(':
                level += 1
                continue
            
            if ch == '(':
                level += 1
            elif ch == ')':
                level -= 1
            
            if level != 0:
                res += ch,
        
        return ''.join(res)


stime = time.time()
print("()()()" == Solution().minAddToMakeValid("(()())(())"))
print("()()()()(())" == Solution().minAddToMakeValid("(()())(())(()(()))"))
print("" == Solution().minAddToMakeValid("()()"))
print('elapse time: {} sec'.format(time.time() - stime))