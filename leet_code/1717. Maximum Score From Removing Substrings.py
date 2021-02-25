import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def dfs(s, score):
            if (s, score) in mem:
                return mem[(s, score)]

            score1 = score2 = 0

            idx1 = s.find('ab')
            if idx1 != -1:
                score1 = dfs(s[:idx1] + s[idx1 + 2:], score + x)

            idx2 = s.find('ba')
            if idx2 != -1:
                score2 = dfs(s[:idx2] + s[idx2 + 2:], score + y)

            if idx1 == -1 and idx2 == -1:
                return score

            mem[(s, score)] = max(score1, score2)
            return mem[(s, score)]

        mem = {}
        return dfs(s, 0)


    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
            1. handle more higher priority first
            2. stk should be used for such a case
                aabb
                aab -> ab -> ''
        """
        prio = ['ab', 'ba'] if x > y else ['ba', 'ab']
        scores = [x, y] if x > y else [y, x]
        tot = 0

        def remove_keyword(s, keyword, score):
            stk  = []
            point = 0

            for ch in s:
                stk += ch,
                if len(stk) < 2:
                    continue

                if ''.join(stk[-2:]) == keyword:
                    stk.pop()
                    stk.pop()
                    point += score

            return point, stk

        stk = list(s)
        
        for prio, score in zip(prio, scores):
            point, stk = remove_keyword(''.join(stk), prio, score)
            tot += point
        return tot


stime = time.time()
print(19 == Solution().maximumGain(s = "cdbcbbaaabab", x = 4, y = 5))
print('elapse time: {} sec'.format(time.time() - stime))