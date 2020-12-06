import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        dp = {}
        operators = {'+', '-', '*'}
        def ops(c, a, b):
            if c == '+':
                return a+b
            elif c == '-':
                return a-b
            elif c == '*':
                return a*b
        
        def helper(s):
            if s not in dp:
                ans = []
                cnt = 0
                for i, c in enumerate(s):
                    if c in operators:
                        cnt += 1
                        for a in helper(s[:i]):
                            for b in helper(s[i+1:]):
                                ans.append(ops(c, a, b))
                if cnt == 0: dp[s] = [int(s)]
                else: dp[s] = ans
            return dp[s]
        

        res = helper(input)
        return res


stime = time.time()
print([0, 2] == Solution().diffWaysToCompute("2-1-1"))
print([-34, -14, -10, -10, 10] == Solution().diffWaysToCompute("2*3-4*5"))
print('elapse time: {} sec'.format(time.time() - stime))
