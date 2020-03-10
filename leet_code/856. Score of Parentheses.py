import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        def dfs(s):
            score = 0
            while s:
                ch = s.pop(0)
                if '(' == ch:
                    score += dfs(s)
                elif ')' == ch:
                    if score:
                        return 2*score
                    return 1
            return score
    
        ret = dfs(list(S))
        return ret
            


stime = time.time()
print(6 == Solution().scoreOfParentheses('(()(()))'))
print('elapse time: {} sec'.format(time.time() - stime))