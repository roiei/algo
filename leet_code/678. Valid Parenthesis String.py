
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def checkValidString(self, s: str) -> bool:
        def dfs(l, r, s, opn):
            if l > r:
                return opn == 0

            res = [False]
            
            if s[l] == '(':
                res += dfs(l + 1, r, s, opn + 1),
            elif s[l] == ')':
                if not opn:
                    return False
                res += dfs(l + 1, r, s, opn - 1),
            elif s[l] == '*':
                s[l] = '('
                res += dfs(l, r, s, opn),
                s[l] = ')'
                res += dfs(l, r, s, opn),
                res += dfs(l + 1, r, s, opn),
            
            return any(res)
        
        return dfs(0, len(s) - 1, list(s), 0)


stime = time.time()
print(True == Solution().checkValidString("(*)"))
print(True == Solution().checkValidString("(*))"))
print('elapse time: {} sec'.format(time.time() - stime))