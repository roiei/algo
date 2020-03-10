import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def numSquares(self, n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        d, q, nq = 1, {n}, set()
        while q:
            for node in q:
                for square in squares:
                    if node == square: return d
                    if node < square: break
                    nq.add(node-square)
            q, nq, d = nq, set(), d+1

    def numSquares(self, n):
        dp = [0] + [float('inf')]*n
        
        for i in range(1, n + 1):
            temp = []
            for j in range(1, int(i**0.5) + 1):
                temp += dp[i - j*j],
                
            dp[i] = min(temp) + 1

        return dp[n]



stime = time.time()
print(3 == Solution().numSquares(12))
print('elapse time: {} sec'.format(time.time() - stime))